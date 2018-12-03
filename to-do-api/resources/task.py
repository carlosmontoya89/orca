from flask_restful import Resource, reqparse
from flask import request
from models.task import TaskModel


class Task(Resource):  


    def post(self):        
        content=request.get_json()       
        task = TaskModel(content["task"])
        try:
            task.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return task.json(), 201

class TaskList(Resource):
    def get(self):
        return {'tasks': list(map(lambda x: x.json(), TaskModel.query.all()))}

