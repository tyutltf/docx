from flask import Flask
from flask_restful import Api, Resource
import request

app = Flask(__name__)
api = Api(app)

users={
    "1":{
        "username":"bob",
        "age":23,
        "sex":"female",
        "phone":13548526584
    },
    "2":{
        "username":"bob",
        "age":18,
        "sex":"male",
        "phone":13548526584
    }
}

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class USERS(Resource):
    def get(self,user_id):
        one_user=users.get(user_id)
        return one_user

    def post(self,user_id):
        print(request.form['data'])
        return ok

api.add_resource(HelloWorld, '/')
api.add_resource(USERS, '/users/<user_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3030, debug=True)
