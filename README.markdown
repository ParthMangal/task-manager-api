# Task Manager API

A Unix-inspired RESTful API for managing tasks, built with Python, FastAPI, and SQLite. This project emulates Unix process operations: `GET /tasks` mirrors `ls` by listing tasks, and `POST /tasks` mimics `fork` by creating new tasks. Tasks are persisted in a SQLite database, ensuring durability across server restarts. The API is designed for simplicity, reliability, and extensibility, with comprehensive documentation, robust error handling, and unit tests.

## Features

- **List Tasks**: `GET /tasks` retrieves all tasks with details (ID, name, description, status, creation time).
- **Create Task**: `POST /tasks` creates a task with a required name and optional description.
- **Persistence**: Tasks are stored in a SQLite database (`tasks.db`) for data durability.
- **Error Handling**: Validates inputs (e.g., non-empty task names) with clear error messages.
- **Testing**: Includes unit tests for core endpoints to ensure functionality.
- **Interactive Documentation**: Swagger UI at `/docs` for easy API exploration.

## Project Structure

```
task-manager-api/
├── src/                     # Application source code
│   ├── __init__.py
│   ├── main.py           # FastAPI application and API routes
│   ├── models.py         # Database schema (Task model)
│   ├── services.py       # Business logic for task operations
│   └── database.py       # Database connection and setup
├── tests/                   # Unit tests
│   ├── __init__.py
│   └── test_api.py       # Tests for API endpoints
├── requirements.txt         # Project dependencies
└── README.md               # Project documentation
```

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Somkar31/task-manager-api.git
   cd task-manager-api
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   uvicorn src.main:app --reload
   ```
   The API is available at `http://localhost:8000`. Access the Swagger UI at `http://localhost:8000/docs`.

5. **Run Tests**:
   ```bash
   pytest tests/
   ```

## API Endpoints

### Create a Task
- **Endpoint**: `POST /tasks`
- **Request Body**:
  ```json
  {
    "name": "My Task",
    "description": "A sample task"
  }
  ```
- **Response** (201 Created):
  ```json
  {
    "id": 1,
    "name": "My Task",
    "description": "A sample task",
    "status": "running",
    "created_at": "2025-02-04T12:00:00.000000"
  }
  ```
- **Error Response** (400 Bad Request):
  ```json
  {
    "detail": "Task name cannot be empty"
  }
  ```

### List Tasks
- **Endpoint**: `GET /tasks`
- **Response** (200 OK):
  ```json
  [
    {
      "id": 1,
      "name": "My Task",
      "description": "A sample task",
      "status": "running",
      "created_at": "2025-02-04T12:00:00.000000"
    }
  ]
  ```
- **Empty Response** (200 OK):
  ```json
  []
  ```

## Usage Examples

### Using `curl`
- **Create a Task**:
  ```bash
  curl -X POST "http://localhost:8000/tasks" -H "Content-Type: application/json" -d '{"name":"Test Task","description":"A test task"}'
  ```
- **List Tasks**:
  ```bash
  curl "http://localhost:8000/tasks"
  ```

### Using PowerShell
PowerShell aliases `curl` to `Invoke-WebRequest`. Use the following:

- **Create a Task**:
  ```powershell
  Invoke-WebRequest -Uri "http://localhost:8000/tasks" -Method POST -Headers @{ "Content-Type" = "application/json" } -Body '{"name":"Test Task","description":"A test task"}'
  ```
- **List Tasks**:
  ```powershell
  Invoke-WebRequest -Uri "http://localhost:8000/tasks" -Method GET
  ```

### Using Postman
- **POST /tasks**: Set the request body to JSON with `name` and optional `description`, and set the `Content-Type` header to `application/json`.
- **GET /tasks**: Send a GET request to retrieve the task list.

## Design Choices

- **FastAPI**: Selected for its high performance, async capabilities, and automatic generation of OpenAPI documentation, streamlining development of a robust RESTful API.
- **SQLite**: A lightweight, serverless database ideal for this project’s scope, storing tasks in `tasks.db` for persistence.
- **SQLAlchemy**: Provides an ORM for clean, database-agnostic interactions, enhancing maintainability.
- **Pydantic**: Ensures type safety and validates request/response data, minimizing errors.
- **Modular Architecture**: Separates concerns (routes in `main.py`, logic in `services.py`, schema in `models.py`, database in `database.py`) for scalability and clarity.
- **Error Handling**: Implements input validation (e.g., non-empty task names) with meaningful HTTP error responses.
- **Testing**: Includes unit tests in `test_api.py` to verify endpoint functionality, ensuring reliability.
- **Unix Inspiration**: `POST /tasks` emulates `fork` by creating tasks with unique IDs, and `GET /tasks` mimics `ls` by listing tasks, aligning with the Unix analogy.

## Potential Enhancements

- **Task States**: Introduce states (e.g., “completed,” “failed”) with background jobs for state transitions.
- **Additional Endpoints**: Add `DELETE /tasks/{id}` (akin to `kill`) or `GET /tasks/{id}` for task details.
- **Filtering**: Support query parameters to filter tasks by status or creation time.
- **Authentication**: Implement token-based authentication for multi-user support.
- **Containerization**: Provide a Dockerfile and `docker-compose.yml` for simplified deployment.
- **Frontend/CLI**: Develop a React frontend or CLI tool, leveraging my experience with React-based biotech applications.

## Notes

- Tasks are persisted in `tasks.db`, ensuring data retention across restarts.
- The Swagger UI at `http://localhost:8000/docs` offers an interactive interface for testing endpoints.
- The project structure supports easy extension for additional features.
- PowerShell’s `curl` alias to `Invoke-WebRequest` is addressed with alternative commands in the usage examples.

## Testing

Verify API functionality with:
```bash
pytest tests/
```
This executes unit tests for task creation, listing, and error handling.

## Troubleshooting

- **API Not Responding**: Ensure the server is running (`uvicorn src.main:app --reload`) and visit `http://localhost:8000/docs`.
- **PowerShell `curl` Issue**: Use `Invoke-WebRequest` commands or run `curl` in Git Bash/WSL.
- **Dependency Errors**: Confirm Python 3.8+ is installed and re-run `pip install -r requirements.txt`.

For further assistance, refer to the [FastAPI documentation](https://fastapi.tiangolo.com/) or contact the repository maintainer.

---
