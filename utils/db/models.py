from datetime import datetime

from flask_login import UserMixin

from server import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    tasks = db.relationship("Tasks")


class Tasks(db.Model):
    STATUSES = {
        0: "During",
        1: "Decided"
    }
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Integer)
    change_time = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
