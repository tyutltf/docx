from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)
parse = reqparse.RequestParser()


# 不带参数
class Hello(Resource):
    def get(self):
        return {'hello': 'get'}

    def post(self):
        return {'hello': 'post'}

    def put(self):
        return {'hello': 'put'}

    def delete(self):
        return {'hello': 'delete'}


users = [
    {
        'userid': 1,
        'username': 'bob',
        'age': 18,
        'sex': 'female',
    },
    {
        'userid': 2,
        'username': 'rose',
        'age': 19,
        'sex': 'male',
    }
]

# 带参数


class USERS(Resource):
    def get(self, userid):
        res = None
        for i in users:
            if str(i.get('userid')) == str(userid):
                res = i
        return res

    def post(self, userid):
        userid = request.form['userid']
        username = request.form['username']
        age = request.form['age']
        sex = request.form['sex']
        new_user = {'userid': userid,
                    'username': username, 'age': age, 'sex': sex}
        users.append(new_user)
        return users

    def put(self, userid):
        userid = request.form['userid']
        age = request.form['age']
        for i in users:
            if str(i.get('userid')) == str(userid):
                i['age'] = age
        return users

    def delete(self, userid):
        userid = request.form['userid']
        for i in users:
            if str(i.get('userid')) == str(userid):
                users.remove(i)
        return users


api.add_resource(Hello, '/')
api.add_resource(USERS, '/users/<userid>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3030, debug=True)
