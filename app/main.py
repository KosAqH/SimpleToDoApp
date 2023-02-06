from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.models import User, Task
from . import db

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    tasks = User.query.filter_by(id=current_user.id).first().tasks
    filtered_tasks = [t for t in tasks if t.status == "Active"]
    return render_template('index.html', tasks=filtered_tasks)

@main.route('/new', methods=['POST'])
@login_required
def new_task_post():
    title = request.form.get('task_title')
    uid = current_user.id

    new_task = Task(user_id = uid, title=title, status = "Active")
    db.session.add(new_task)
    db.session.commit()

    return redirect(url_for('main.index'))

@main.route('/remove', methods=["POST"])
@login_required
def remove_task():
    id = request.form.get("task_id")
    task = Task.query.filter_by(id=id).first()
    task.status = "Finished"

    db.session.commit()
    return redirect(url_for('main.index'))
