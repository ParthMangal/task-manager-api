from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks", json={"name": "Test Task", "description": "A test task"})
    assert response.status_code == 201
    assert response.json()["name"] == "Test Task"
    assert response.json()["status"] == "running"

def test_create_task_empty_name():
    response = client.post("/tasks", json={"name": "", "description": "Invalid task"})
    assert response.status_code == 400
    assert "Task name cannot be empty" in response.json()["detail"]

def test_list_tasks():
    # Create a task first
    client.post("/tasks", json={"name": "Task 1", "description": "First task"})
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1