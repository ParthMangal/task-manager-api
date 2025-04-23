from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from .services import create_task, get_all_tasks
from .database import init_db

app = FastAPI(title="Task Manager API")

# Pydantic model for task creation
class TaskCreate(BaseModel):
    name: str
    description: str = ""

# Pydantic model for task response
class TaskResponse(BaseModel):
    id: int
    name: str
    description: str
    status: str
    created_at: str

@app.on_event("startup")
async def startup_event():
    init_db()  # Initialize database on startup

@app.post("/tasks", response_model=TaskResponse, status_code=201)
async def create_task_endpoint(task: TaskCreate):
    try:
        new_task = create_task(task.name, task.description)
        return new_task
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/tasks", response_model=List[TaskResponse])
async def list_tasks_endpoint():
    tasks = get_all_tasks()
    return tasks