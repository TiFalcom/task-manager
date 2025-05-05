from app.crud.task import TaskManager
from app.database import create_tables
from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
def startup():
    create_tables()

@app.get('/ping')
def read_root():
    return {'message': 'Pong!'}

@app.post('/tasks/add')
def add_task(task: str):
    TaskManager.add_task(task)
    return {'message': f'Task "{task}" added.'}

@app.delete('/tasks/remove')
def remove_task(task: str):
    response = TaskManager.remove_task(task)
    if response is None:
        return {'message': f'Task "{task}" not found.'}
    return {'message': f'Task "{task}" removed.'}

@app.get('/tasks/list')
def list_tasks():
    tasks = TaskManager.list_tasks()
    return {'tasks': tasks}