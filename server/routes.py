from flask import Blueprint

app = Blueprint('server_app', __name__)


@app.route("/create", methods=['POST'])
def create():
    pass


@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):
    pass


@app.route("/edit/<int:task_id>", methods=['POST'])
def update(task_id):
    pass
