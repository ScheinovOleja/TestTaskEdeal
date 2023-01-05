from flask import Blueprint, request, jsonify

from utils.db import database as db

app = Blueprint('server_app', __name__)


@app.route("/create", methods=['POST'])
def create():
    data = request.get_json()
    task_id = db.create_new_task(data['description'])
    result = {"Success": True, "Response": f"New task successfully created. Task_id - {task_id}"}
    return jsonify(result)


@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):
    try:
        db.remove_task(task_id)
        result = {"Success": True, "Response": f"Task successfully removed."}
    except:
        result = {"Success": False, "Response": "Something went wrong"}
    return jsonify(result)


@app.route("/edit/description/<int:task_id>", methods=['POST'])
def update_description(task_id):
    data = request.get_json()
    try:
        db.update_task_description(task_id, data['description'])
        result = {"Success": True, "Response": f"Task description successfully updated."}
    except:
        result = {"Success": False, "Response": "Something went wrong"}
    return jsonify(result)


@app.route("/edit/status/<int:task_id>", methods=['POST'])
def update_status(task_id):
    data = request.get_json()
    try:
        db.update_task_status(task_id, data['status'])
        result = {"Success": True, "Response": f"Task status successfully updated."}
    except:
        result = {"Success": False, "Response": "Something went wrong"}
    return jsonify(result)
