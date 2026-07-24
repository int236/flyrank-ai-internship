# Task API with SQLite
---

## Features
- Create tasks
- Read all tasks
- Read a task by ID
- Update tasks
- Delete tasks
- Persistent storage using SQLite
- Interactive API documentation with Swagger UI

---

## Why SQLite?
SQLite is a lightweight, serverless relational database that stores data inside a single file. It requires no separate installation and is ideal for small applications and learning backend development.

---

## Database
The database file is automatically created when the application starts.
```
tasks.db
```
The application also automatically creates the `tasks` table if it does not exist and inserts three sample tasks only on the first run.

---

## Installation
```bash
pip install -r requirements.txt
```

---
## Run
```bash
uvicorn app:app --reload
```

Server:
```
http://127.0.0.1:8000
```

Swagger UI:
```
http://127.0.0.1:8000/docs
```

---
## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information |
| GET | `/health` | Health check |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{task_id}` | Get a task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

---
## Example SQL Queries
List all tasks
```sql
SELECT * FROM tasks;
```
Completed tasks
```sql
SELECT * FROM tasks WHERE done = 1;
```
Count tasks
```sql
SELECT COUNT(*) FROM tasks;
```
---

## Project Structure
```
backend-api/
│
├── app.py
├── tasks.db
├── requirements.txt
├── README.md
└── images/
    └── swagger.png
```

---

## Swagger UI
Interactive API documentation:
```
http://127.0.0.1:8000/docs
```

Add your screenshot here:
```md
![Swagger UI](images/swagger.png)
```

---

## Technologies Used

- Python
- FastAPI
- SQLite
- Uvicorn
- Pydantic
