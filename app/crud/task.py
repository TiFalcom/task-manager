from app.models.task import Task
from app.database import get_session

class TaskManager:

    @staticmethod
    def add_task(task: str):
        with get_session() as session:
            new_task = Task(title=task)
            session.add(new_task)
        return task

    @staticmethod
    def remove_task(task: str):
        with get_session() as session:
            task_to_remove = session.query(Task).filter(Task.title == task).first()
            if task_to_remove:
                session.delete(task_to_remove)
                return task
            return None

    @staticmethod
    def list_tasks():
        with get_session() as session:
            return [
                {"id" : task.id, "title" : task.title} 
                for task in session.query(Task).all()
            ]
