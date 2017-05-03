from flask import jsonify
from flask_restful import Resource, Api

class CourseList(Resource):
    def get(self):
        return jsonify({'CourseList'})

class Course(Resource):

    def get(self):
        return jsonify({'Course'})

    def put(self):
        return jsonify({'Course'})

    def delete(self):
        return jsonify({'Course'})

