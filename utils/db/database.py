from utils.db.models import Tasks
from utils.decorators import session_action


@session_action
def create_new_task(text: str) -> tuple[Tasks, str]:
    from datetime import datetime
    new_task = Tasks(task=text, status=0, change_time=datetime.now())
    return new_task, "add"


@session_action
def remove_task(task_id: int) -> tuple[str, str]:
    query = f"DELETE FROM tasks WHERE id={task_id};"
    return query, "execute"


@session_action
def update_task_description(task_id: int, description: str) -> tuple[str, str]:
    from datetime import datetime
    query = f"UPDATE tasks SET task = '{description}', change_time = '{datetime.now()}' WHERE id = {task_id}"
    return query, "execute"


@session_action
def update_task_status(task_id: int, status: int) -> tuple[str, str]:
    from datetime import datetime
    query = f"UPDATE tasks SET status = '{status}', change_time = '{datetime.now()}' WHERE id = {task_id}"
    return query, "execute"
