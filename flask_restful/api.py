from flask import Flask,request
from flask_restful import Api, Resource,reqparse

app = Flask(__name__)
api = Api(app)
parse = reqparse.RequestParser()

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

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class USERS(Resource):
    def get(self,userid):
        res=None
        for i in users:
            if str(i.get('userid'))==str(userid):
                res=i
        return res

    def post(self,userid):
        userid=request.form['userid']
        username=request.form['username']
        age=request.form['age']
        sex=request.form['sex']
        new_user={'userid':userid,'username':username,'age':age,'sex':sex}
        users.append(new_user)
        return users

    def put(self,userid):
        userid=request.form['userid']
        age=request.form['age']
        for i in users:
            if str(i.get('userid'))==str(userid):
                i['age']=age
        return users

    def delete(self,userid):
        pass

api.add_resource(HelloWorld, '/')
api.add_resource(USERS, '/users/<userid>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3030, debug=True)
