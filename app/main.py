from fastapi import FastAPI
from app.database import create_tables
from app.routers import task

app = FastAPI()

@app.on_event("startup")
def startup():
    create_tables()

@app.get('/ping')
def read_root():
    return {'message': 'Pong!'}

app.include_router(task.router, prefix="/task", tags=["Task"])
