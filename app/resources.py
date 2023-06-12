from flask_restful import Resource, reqparse
from .models import db, Task
from flask import jsonify
from datetime import datetime
from sqlalchemy import desc

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, help='Title is required')
parser.add_argument('description', type=str)
parser.add_argument('due_date', type=str, help='Due date must be in YYYY-MM-DD format')

status_parser = reqparse.RequestParser()
status_parser.add_argument('status', type=str, required=True, 
                           choices=["Incomplete", "Completed", "In Progress"], 
                           help='Status is required and Should be one of Incomplete, Completed, In Progress')


class TasksResource(Resource):
    def get(self):
        tasks = Task.query.order_by(Task.created_at).all()
        return jsonify([task.to_dict() for task in tasks])
    
    def post(self):
        args = parser.parse_args()
        task = Task(
            title=args['title'], 
            description=args['description'], 
            due_date=datetime.strptime(args['due_date'], '%Y-%m-%d')
            )
        db.session.add(task)
        db.session.commit()
        return jsonify({
            "message": "Task created successfully", 
            "task": task.to_dict()
            })

class TaskResource(Resource):
    def get(self, task_id):
        task = Task.query.filter_by(id=task_id).first()
        return jsonify(task.to_dict())
    
    def put(self, task_id):
        args = parser.parse_args()
        task = Task.query.filter_by(id=task_id).first()
        task.title = args['title']
        task.description = args['description']
        task.due_date = datetime.strptime(args['due_date'], '%Y-%m-%d')
        db.session.commit()
        return jsonify({
            "message": "Task updated successfully",
            "task": task.to_dict()
            })
    
    def delete(self, task_id):
        task = Task.query.filter_by(id=task_id).first()
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deleted successfully"})

class TaskStatusResource(Resource):
    def put(self,task_id):
        args = status_parser.parse_args()
        task = Task.query.filter_by(id=task_id).first()
        task.status = args['status']
        db.session.commit()
        return jsonify({
            "message": "Task status updated successfully",
            "task": task.to_dict()
            })