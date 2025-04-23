from sqlalchemy.orm import Session
from .models import Task
from .database import get_db
from datetime import datetime
from typing import List

def create_task(name: str, description: str) -> dict:
    if not name.strip():
        raise ValueError("Task name cannot be empty")
    
    db = next(get_db())
    task = Task(name=name, description=description, status="running")
    db.add(task)
    db.commit()
    db.refresh(task)
    
    return {
        "id": task.id,
        "name": task.name,
        "description": task.description,
        "status": task.status,
        "created_at": task.created_at.isoformat()
    }

def get_all_tasks() -> List[dict]:
    db = next(get_db())
    tasks = db.query(Task).all()
    return [
        {
            "id": task.id,
            "name": task.name,
            "description": task.description,
            "status": task.status,
            "created_at": task.created_at.isoformat()
        }
        for task in tasks
    ]