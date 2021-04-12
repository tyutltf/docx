from flask import Flask, request
from flask_restful import Api, reqparse, OrderedDict
from werkzeug.wrappers import Response as ResponseBase

try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping

app = Flask(__name__)
api = Api(app)


def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    """用元类创建一个类"""
    # This requires a bit of explanation: the basic idea is to make a
    # dummy metaclass for one level of class instantiation that replaces
    # itself with the actual metaclass.
    class metaclass(type):
        def __new__(metacls, name, this_bases, d):
            return meta(name, bases, d)

    return type.__new__(metaclass, "temporary_class", (), {})


# 构建一个不可变集合
http_method_funcs = frozenset(
    ["get", "post", "head", "options", "delete", "put", "trace", "patch"]
)


class View(object):
    """Alternative way to use view functions.  A subclass has to implement
    :meth:`dispatch_request` which is called with the view arguments from
    the URL routing system.  If :attr:`methods` is provided the methods
    do not have to be passed to the :meth:`~flask.Flask.add_url_rule`
    method explicitly::
    视图函数的另一种使用方式。
    子类必须实现哪个是用视图参数调用的URL路由系统。
        class MyView(View):
            methods = ['GET']

            def dispatch_request(self, name):
                return 'Hello %s!' % name

        app.add_url_rule('/hello/<name>', view_func=MyView.as_view('myview'))

    When you want to decorate a pluggable view you will have to either do that
    when the view function is created (by wrapping the return value of
    :meth:`as_view`) or you can use the :attr:`decorators` attribute::
    当你想装饰一个可插入的视图时，你必须这样做，当创建view函数时
        class SecretView(View):
            methods = ['GET']
            decorators = [superuser_required]

            def dispatch_request(self):
                ...

    The decorators stored in the decorators list are applied one after another
    when the view function is created.  Note that you can *not* use the class
    based decorators since those would decorate the view class and not the
    generated view function!
    当创建view函数时，decorator列表中存储的decorator将一个接一个地应用。
    注意，你不能使用基于类的装饰器，因为那些装饰的是视图类，而不是生成的视图函数!
    """

    #: A list of methods this view can handle.
    methods = None

    #: Setting this disables or force-enables the automatic options handling.
    # 设置此选项将禁用或强制启用自动选项处理。
    provide_automatic_options = None

    # The canonical way to decorate class-based views is to decorate the return value of as_view().
    # 装饰基于类的视图的规范方法是装饰as_view()的返回值。
    # However since this moves parts of the logic from the class declaration to the place where it's hooked into the routing system.
    # 但是，这将把部分逻辑从类声明移动到与路由系统相连的地方。
    # You can place one or more decorators in this list and whenever the view function is created the result is automatically decorated.
    # 您可以在这个列表中放置一个或多个装饰器，当视图函数被创建时，结果就会被自动装饰。
    decorators = ()

    def dispatch_request(self):
        """Subclasses have to override this method to implement the
        actual view function code.  This method is called with all
        the arguments from the URL rule.
        子类必须重写此方法来实现实际的视图函数代码。
        这个方法被来自URL规则的所有参数调用。
        """
        raise NotImplementedError()

    @classmethod
    def as_view(cls, name, *class_args, **class_kwargs):
        """Converts the class into an actual view function that can be used
        with the routing system.  
        将类转换为可使用的实际视图函数路由系统。
        Internally this generates a function on the fly which will instantiate the :class:`View` on each request and call
        the :meth:`dispatch_request` method on it.
        在内部，它会动态生成一个函数来实例化，
        The arguments passed to :meth:`as_view` are forwarded to the
        constructor of the class.
        """

        def view(*args, **kwargs):
            self = view.view_class(*class_args, **class_kwargs)
            return self.dispatch_request(*args, **kwargs)

        if cls.decorators:
            view.__name__ = name
            view.__module__ = cls.__module__
            for decorator in cls.decorators:
                view = decorator(view)

        # We attach the view class to the view function for two reasons:
        # 我们将view类附加到view函数有两个原因
        # first of all it allows us to easily figure out what class-based view this thing came from,
        # 首先，它允许我们很容易地找出这个东西来自什么基于类的视图，
        # secondly it's also used for instantiating the view class so you can actually replace it with something else for testing purposes and debugging.
        # 其次，它也用于实例化视图类，这样你就可以用其他的东西来代替它，以进行测试和调试。
        view.view_class = cls
        view.__name__ = name
        view.__doc__ = cls.__doc__
        view.__module__ = cls.__module__
        view.methods = cls.methods
        view.provide_automatic_options = cls.provide_automatic_options
        return view


class MethodViewType(type):
    """Metaclass for :class:`MethodView` that determines what methods the view
    defines.
    类 MethodView 决定这个视图定义的方法
    """

    def __init__(cls, name, bases, d):
        super(MethodViewType, cls).__init__(name, bases, d)

        if "methods" not in d:
            methods = set()

            for base in bases:
                if getattr(base, "methods", None):
                    methods.update(base.methods)

            for key in http_method_funcs:
                if hasattr(cls, key):
                    methods.add(key.upper())

            if methods:
                cls.methods = methods


class MethodView(with_metaclass(MethodViewType, View)):
    """A class-based view that dispatches request methods to the corresponding
    class methods. For example, if you implement a ``get`` method, it will be
    used to handle ``GET`` requests. ::
    一种基于类的视图，将请求方法分派给相应的类方法。例如，如果实现一个``get``方法，它将
    用于处理“GET”请求。

        class CounterAPI(MethodView):
            def get(self):
                return session.get('counter', 0)

            def post(self):
                session['counter'] = session.get('counter', 0) + 1
                return 'OK'

        app.add_url_rule('/counter', view_func=CounterAPI.as_view('counter'))
    """

    def dispatch_request(self, *args, **kwargs):
        meth = getattr(self, request.method.lower(), None)

        # If the request method is HEAD and we don't have a handler for it
        # retry with GET.
        if meth is None and request.method == "HEAD":
            meth = getattr(self, "get", None)

        assert meth is not None, "Unimplemented method %r" % request.method
        return meth(*args, **kwargs)


class Resource(MethodView):
    """
    Represents an abstract RESTful resource. Concrete resources should
    extend from this class and expose methods for each supported HTTP
    method. If a resource is invoked with an unsupported HTTP method,
    the API will return a response with status 405 Method Not Allowed.
    Otherwise the appropriate method is called and passed all arguments
    from the url rule used when adding the resource to an Api instance. See
    :meth:`~flask_restful.Api.add_resource` for details.
    表示抽象的RESTful资源。具体资源应
    从此类扩展并为每个受支持的HTTP
    方法。如果使用不受支持的HTTP方法调用资源，
    API将返回一个状态为405 Method Not Allowed的响应。
    否则，将调用相应的方法并将其传递给所有参数
    从将资源添加到Api实例时使用的url规则
    """

    representations = None
    method_decorators = []

    # 重写MethodView 类的 此方法
    def dispatch_request(self, *args, **kwargs):

        # Taken from flask 这部分是为了拿到request.method 的请求方法
        meth = getattr(self, request.method.lower(), None)
        if meth is None and request.method == 'HEAD':
            meth = getattr(self, 'get', None)
        assert meth is not None, 'Unimplemented method %r' % request.method

        # 判断方法method_decorators 是否是映射类型
        if isinstance(self.method_decorators, Mapping):
            decorators = self.method_decorators.get(request.method.lower(), [])
        else:
            decorators = self.method_decorators
        for decorator in decorators:
            meth = decorator(meth)
        print(meth)
        resp = meth(*args, **kwargs)
        print(resp)
        if isinstance(resp, ResponseBase):
            return resp

        representations = self.representations or OrderedDict()
        mediatype = request.accept_mimetypes.best_match(
            representations, default=None)
        print(mediatype)
        if mediatype in representations:
            data, code, headers = unpack(resp)
            resp = representations[mediatype](data, code, headers)
            resp.headers['Content-Type'] = mediatype
            return resp
        return resp


# 不带参数
class Hello(Resource):
    def get(self):
        return {'hello': 'get'}

    def post(self):
        return {'hello': 'post'}


api.add_resource(Hello, '/hello')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3131, debug=True)
