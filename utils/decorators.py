from server import db


def delete_later_30_days(func):
    def delete_entry(*args, **kwargs):
        query = "DELETE FROM tasks WHERE status == 1 AND julianday('now') - julianday(change_time) >= 30"
        db.session.execute(query)
        db.session.commit()
        return func(*args, **kwargs)

    delete_entry.__name__ = func.__name__
    return delete_entry


def session_action(func):
    def commit_database(*args, **kwargs):
        obj, action = func(*args, **kwargs)
        if action == "execute":
            db.session.execute(obj)
        elif action == "add":
            db.session.add(obj)
        else:
            return
        db.session.commit()

    commit_database.__name__ = func.__name__
    return commit_database
