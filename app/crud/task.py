from app.database import engine, Task
from sqlalchemy.orm import sessionmaker

class TaskManager:
    session = sessionmaker(bind=engine)()

    @classmethod
    def _commit_close_session(cls):
        """Commit the session and close it."""
        cls.session.commit()
        cls.session.close()

    @classmethod
    def add_task(cls, task : str):
        new_task = Task(title=task)
        cls.session.add(new_task)
        cls._commit_close_session()
        return task

    @classmethod
    def remove_task(cls, task : str):
        task_to_remove = cls.session.query(Task).filter(Task.title == task).first()
        if task_to_remove:
            cls.session.delete(task_to_remove)
            cls._commit_close_session()
            return task
        else:
            cls._commit_close_session()
            return None
        

    @classmethod
    def list_tasks(cls):
        tasks = cls.session.query(Task).all()
        cls._commit_close_session()
        return tasks