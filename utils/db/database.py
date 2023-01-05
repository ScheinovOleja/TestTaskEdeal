from server import db
from utils.db.models import Tasks


def create_new_task(text: str) -> int:
    from datetime import datetime
    new_task = Tasks(task=text, status=0, change_time=datetime.now())
    db.session.add(new_task)
    db.session.commit()
    return new_task.id
