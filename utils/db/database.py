from server import db
from utils.db.models import Tasks
from utils.decorators import session_action


def create_new_task(text: str) -> None:
    from datetime import datetime
    new_task = Tasks(task=text, status=0, change_time=datetime.now())
    db.session.add(new_task)
    db.session.commit()


@session_action
def remove_task(task_id: int) -> str:
    query = f"DELETE FROM tasks WHERE id={task_id};"
    return query


@session_action
def update_task_description(task_id: int, description: str) -> str:
    from datetime import datetime
    query = f"UPDATE tasks SET task = '{description}', change_time = '{datetime.now()}' WHERE id = {task_id}"
    return query


@session_action
def update_task_status(task_id: int, status: int) -> str:
    from datetime import datetime
    query = f"UPDATE tasks SET status = '{status}', change_time = '{datetime.now()}' WHERE id = {task_id}"
    return query
