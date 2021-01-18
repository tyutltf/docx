from functools import wraps

from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
# 定义传入的参数格式
parser.add_argument('userid', type=int,help='id must be an integert')
parser.add_argument('username', type=str)
parser.add_argument('age', type=int)
parser.add_argument('sex', type=str)

def demo_Ornament(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not kwargs:
            return 'args is none'
        return func(*args, **kwargs)
    return wrapper

class Resource(Resource):
    method_decorators = [demo_Ornament]

# 不带参数
class Hello(Resource):
    def get(self):
        return {'hello': 'get'}

    def post(self):
        return {'hello': 'post'}

users=[
    {
        'userid':1,
        'username':'bob',
        'age':18,
        'sex':'female',
    },
    {
        'userid':2,
        'username':'rose',
        'age':19,
        'sex':'male',
    }
]

# 带参数
class Users(Resource):
    def get(self,userid):
        args = parser.parse_args()
        res=None
        for i in users:
            if i.get('userid')==args['userid']:
                res=i
        return res

    def post(self,userid):
        args = parser.parse_args()
        new_user={'userid':args['userid'],'username':args['username'],'age':args['age'],'sex':args['sex']}
        users.append(new_user)
        return users


api.add_resource(Hello, '/')
api.add_resource(Users, '/users','/users/<userid>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3030, debug=True)
