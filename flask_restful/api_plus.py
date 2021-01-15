from flask import Flask,request
from flask_restful import Api, Resource,reqparse

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