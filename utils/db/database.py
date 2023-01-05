from server import db
from utils.db.models import Tasks


def create_new_task(text: str) -> int:
    from datetime import datetime
    new_task = Tasks(task=text, status=0, change_time=datetime.now())
    db.session.add(new_task)
    db.session.commit()
    return new_task.id


def remove_task(task_id: int) -> None:
    query = f"DELETE FROM tasks WHERE id={task_id};"
    db.session.execute(query)
    db.session.commit()


def update_task_description(task_id: int, description: str) -> None:
    from datetime import datetime
    query = f"UPDATE tasks SET task = '{description}', change_time = '{datetime.now()}' WHERE id = {task_id}"
    db.session.execute(query)
    db.session.commit()


def update_task_status(task_id: int, status: int) -> None:
    from datetime import datetime
    query = f"UPDATE tasks SET status = '{status}', change_time = '{datetime.now()}' WHERE id = {task_id}"
    db.session.execute(query)
    db.session.commit()
