from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# from app import db
# db.create_all()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(2-0), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        task = Todo(content=task_content)
        try:
            db.session.add(task)
            db.session.commit()
        except:
            print("Not added")

        return redirect(url_for('index'))
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task = Todo.query.get_or_404(id)

    try:
        db.session.delete(task)
        db.session.commit()

    except:
        print("Not deleted")

    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
        except:
            print("Not updated")
        return redirect(url_for('index'))
    else:
        return render_template('update.html', task=task)

# make the database json and send back in flask app
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = Todo.query.all()
    task_list = []
    for task in tasks:
        task_list.append({
            'id': task.id,
            'content': task.content,
            'completed': task.completed,
            'date_created': task.date_created
        })
    return jsonify({'tasks': task_list})

if __name__ == "__main__":
    app.run(debug=True)
