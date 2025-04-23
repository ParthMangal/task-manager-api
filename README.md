Task Manager API
A Unix-inspired Task Manager API built with Python, FastAPI, and SQLite. This project mimics Unix process operations, where GET /tasks resembles ls (listing tasks) and POST /tasks emulates fork (creating a new task). Tasks are persisted in a SQLite database, ensuring data survives server restarts. The API is designed to be intuitive, robust, and well-documented, with unit tests to verify functionality.
Features

List Tasks: GET /tasks - Returns a list of all tasks with details (ID, name, description, status, creation time).
Create Task: POST /tasks - Creates a new task with a name and optional description, returning the task’s details.
Persistence: Tasks are stored in a SQLite database (tasks.db) for durability.
Error Handling: Validates inputs (e.g., non-empty task names) and returns clear error messages.
Testing: Includes unit tests for core API endpoints to ensure reliability.
Documentation: Swagger UI at /docs for interactive API exploration.

Project Structure
task-manager-api/
├── src/                     # Core application code
│   ├── __init__.py
│   ├── main.py           # FastAPI app and API routes
│   ├── models.py         # Database schema (Task model)
│   ├── services.py       # Business logic for task operations
│   └── database.py       # Database connection and setup
├── tests/                   # Unit tests
│   ├── __init__.py
│   └── test_api.py       # Tests for API endpoints
├── requirements.txt         # Dependencies
└── README.md               # This file

Setup Instructions

Clone the Repository:
git clone <repository-url>
cd task-manager-api


Create a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Run the Application:
uvicorn src.main:app --reload

The API will be available at http://localhost:8000. Visit http://localhost:8000/docs for the Swagger UI.

Run Tests:
pytest tests/



API Endpoints
Create a Task

Endpoint: POST /tasks
Request Body:{
  "name": "My Task",
  "description": "A sample task"
}


Response (201 Created):{
  "id": 1,
  "name": "My Task",
  "description": "A sample task",
  "status": "running",
  "created_at": "2025-02-04T12:00:00.000000"
}


Error Response (400 Bad Request):{
  "detail": "Task name cannot be empty"
}



List Tasks

Endpoint: GET /tasks
Response (200 OK):[
  {
    "id": 1,
    "name": "My Task",
    "description": "A sample task",
    "status": "running",
    "created_at": "2025-02-04T12:00:00.000000"
  }
]


Empty Response (200 OK):[]



Usage Examples
Using curl

Create a task:curl -X POST "http://localhost:8000/tasks" -H "Content-Type: application/json" -d '{"name":"Test Task","description":"A test task"}'


List tasks:curl "http://localhost:8000/tasks"



Using PowerShell
Since PowerShell aliases curl to Invoke-WebRequest, use:

Create a task:Invoke-WebRequest -Uri "http://localhost:8000/tasks" -Method POST -Headers @{ "Content-Type" = "application/json" } -Body '{"name":"Test Task","description":"A test task"}'


List tasks:Invoke-WebRequest -Uri "http://localhost:8000/tasks" -Method GET



Using Postman

POST /tasks: Set the body to JSON with name and description, and Content-Type: application/json.
GET /tasks: Send a GET request to retrieve the task list.

Design Choices

FastAPI: Chosen for its simplicity, async support, and automatic OpenAPI documentation, enabling rapid development of a clean RESTful API.
SQLite: A lightweight, serverless database suitable for this project’s scope. Persists tasks in tasks.db for durability.
SQLAlchemy: Provides an ORM for clean database interactions, making the code maintainable and database-agnostic.
Pydantic: Ensures type safety and validates request/response data, reducing errors.
Modular Structure: Separates routes (main.py), business logic (services.py), models (models.py), and database setup (database.py) for clarity and scalability.
Error Handling: Validates inputs (e.g., non-empty task names) and returns meaningful HTTP errors (e.g., 400 Bad Request).
Testing: Includes unit tests (test_api.py) to verify API functionality, demonstrating reliability.
Unix Inspiration: POST /tasks mimics fork by creating a task with a unique ID, and GET /tasks resembles ls by listing tasks, making the API intuitive.

Potential Enhancements

Task States: Add states like “completed” or “failed” with background jobs to simulate state transitions.
Additional Endpoints: Implement DELETE /tasks/{id} (like kill) or GET /tasks/{id} for task details.
Filtering: Support query parameters for filtering tasks (e.g., by status or creation time).
Authentication: Add API token-based authentication for multi-user support.
Containerization: Provide a Dockerfile and docker-compose.yml for easy deployment.
Frontend/CLI: Build a simple React frontend or CLI tool to interact with the API, leveraging my experience with React-based biotech tools.

Notes

The API stores tasks in tasks.db, ensuring persistence across restarts.
The Swagger UI at http://localhost:8000/docs provides an interactive way to test endpoints.
The project is designed to be extensible, with a clear structure for adding new features.
The PowerShell curl issue (aliasing to Invoke-WebRequest) is addressed with alternative commands in the usage examples.

Running Tests
To verify the API works as expected:
pytest tests/

This runs unit tests for task creation, listing, and error handling.
Troubleshooting

API not responding: Ensure the server is running (uvicorn src.main:app --reload) and check http://localhost:8000/docs.
PowerShell curl issue: Use Invoke-WebRequest as shown above or run curl in Git Bash/WSL.
Dependency errors: Verify Python 3.8+ and re-run pip install -r requirements.txt.

For any issues, consult the FastAPI documentation or contact me for assistance.
Happy coding! 🚀
