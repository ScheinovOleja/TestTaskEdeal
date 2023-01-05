from flask import Blueprint, request, jsonify

from utils.db import database as db
from utils.decorators import delete_later_30_days

app = Blueprint('server_app', __name__)


@app.route("/create", methods=['POST'])
@delete_later_30_days
def create():
    data = request.get_json()
    db.create_new_task(data['description'])
    result = {"Success": True, "Response": f"New task successfully created."}
    return jsonify(result)


@app.route("/delete/<int:task_id>", methods=['POST'])
@delete_later_30_days
def delete(task_id):
    try:
        db.remove_task(task_id)
        result = {"Success": True, "Response": f"Task successfully removed."}
    except:
        result = {"Success": False, "Response": "Something went wrong"}
    return jsonify(result)


@app.route("/edit/<int:task_id>", methods=["POST"])
@delete_later_30_days
def update(task_id):
    data = request.get_json()
    try:
        if data['description']:
            db.update_task_description(task_id, data['description'])
            result = {"Success": True, "Response": "Task description successfully updated."}
        elif data['status']:
            db.update_task_status(task_id, data['status'])
            result = {"Success": True, "Response": "Task status successfully updated."}
        else:
            result = {"Success": False, "Response": "No data to update"}
    except:
        result = {'success': False, 'Response': 'Something went wrong'}
    return jsonify(result)


@app.route("/get/<int:task_id>", methods=["GET"])
def get(task_id):
    task = db.get_task(task_id)
    from utils.db.models import Tasks
    result = {
        "Success": True,
        "Response": {
            "Description": task[0],
            "Status": Tasks.STATUSES[task[1]]
        }
    }
    return jsonify(result)
