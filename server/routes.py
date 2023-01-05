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
    pass


@app.route("/edit/<int:task_id>", methods=['POST'])
def update(task_id):
    pass
