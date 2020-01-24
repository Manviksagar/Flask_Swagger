from flask import Flask, request
from flask_restful import Resource, Api
from flasgger import Swagger
from flask_restful_swagger import swagger
app=Flask(__name__)

api=Api(app)


api=swagger.docs(Api(app), apiVersion='1',api_spec_url="/docs")

class hello(Resource):
    @swagger.model
    @swagger.operation(notes='swagger notes for get Api')
    def get(self):
        return {"about":"Hello world"}

    @swagger.model
    @swagger.operation(notes='swagger notes for Post Api')
    def post(self):
        some_json= request.get_json()
        return {"you_sent":some_json}, 201


class mult(Resource):
    @swagger.model
    @swagger.operation(notes='swagger notes for Class Api')
    def get(self,num):
        return {"result": num*10}

api.add_resource(hello, '/')
api.add_resource(mult, '/mult/<int:num>')


if __name__ == '__main__':
   app.run(debug = True)