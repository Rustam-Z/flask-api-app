# Server Restful API

from flask import Flask, jsonify
from flask_restful import reqparse, Api, Resource
from models import Todo, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

with app.app_context():
    db.create_all()
    
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')


# https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/

# def abort_if_todo_doesnt_exist(todo_id):
#     task = Todo.query.get_or_404(todo_id)
#     return task


# Todo
# shows a single todo item and lets you update / delete a todo item
class Task(Resource):
    def get(self, task_id):
        task = Todo.query.get_or_404(task_id)
        return jsonify(task.serialize())

    def delete(self, task_id):
        task = Todo.query.get_or_404(task_id)

        try:
            db.session.delete(task)
            db.session.commit()
            return jsonify({'success': "Deleted successfully"})
        except:
            return jsonify({'error': 'Not deleted'})

    def put(self, task_id):
        task = Todo.query.get_or_404(task_id)
        task.content = parser.parse_args()['task']

        try:
            db.session.commit()
            return jsonify(Todo.query.get(task.id).serialize())
        except:
            print("Not updated")
            return jsonify({'error': 'Not updated'})

# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TasksList(Resource):
    def get(self):
        tasks = Todo.query.all()
        # return jsonify([task.serialize() for task in tasks])

        tasks_list = []
        for task in tasks:
            tasks_list.append({
                'id': task.id,
                'content': task.content,
                'completed': task.completed,
                'date_created': task.date_created
            })
        return jsonify({'tasks': tasks_list})

    def post(self):
        task_content = parser.parse_args()['task']
        task = Todo(content=task_content)
        try:
            db.session.add(task)
            db.session.commit()
            return jsonify(Todo.query.get(task.id).serialize())
        except:
            return jsonify({'error': 'Not added'})

# Endpoints
api.add_resource(TasksList, '/tasks')
api.add_resource(Task, '/tasks/<task_id>')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
