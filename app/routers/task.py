from fastapi import APIRouter
from app.crud.task import TaskManager
from app.schemas.task import TaskRequest

router = APIRouter()

@router.post('/add')
def add_task(task: TaskRequest):
    TaskManager.add_task(task.title)
    return {'message': f'Task "{task.title}" added.'}

@router.delete('/remove')
def remove_task(task: TaskRequest):
    if not TaskManager.remove_task(task.title):
        return {'message': f'Task "{task.title}" not found.'}
    return {'message': f'Task "{task.title}" removed.'}

@router.get('/list')
def list_tasks():
    tasks = TaskManager.list_tasks()
    return {'tasks': tasks}
