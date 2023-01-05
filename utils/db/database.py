from utils.db.models import Tasks
from utils.decorators import session_action


@session_action("add")
def create_new_task(text: str) -> Tasks:
    from datetime import datetime
    new_task = Tasks(task=text, status=0, change_time=datetime.now())
    return new_task


@session_action("execute")
def remove_task(task_id: int) -> str:
    query = f"DELETE FROM tasks WHERE id={task_id};"
    return query


@session_action("execute")
def update_task_description(task_id: int, description: str) -> str:
    from datetime import datetime
    query = f"UPDATE tasks SET task = '{description}', change_time = '{datetime.now()}' WHERE id = {task_id}"
    return query


@session_action("execute")
def update_task_status(task_id: int, status: int) -> str:
    from datetime import datetime
    query = f"UPDATE tasks SET status = '{status}', change_time = '{datetime.now()}' WHERE id = {task_id}"
    return query


@session_action("get")
def get_task(task_id: int) -> str:
    query = f"SELECT task, status FROM tasks WHERE id={task_id}"
    return query

