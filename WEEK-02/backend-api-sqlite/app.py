import sqlite3
from fastapi import FastAPI, HTTPException

app = FastAPI()

DB_NAME = "tasks.db"

conn = sqlite3.connect(DB_NAME, check_same_thread=False)
cursor = conn.cursor()

cursor.execute(
"""CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done BOOLEAN NOT NULL
)"""
)
conn.commit()

cursor.execute("SELECT COUNT(*) FROM tasks")
count = cursor.fetchone()[0]    
if count == 0:
    cursor.executemany("INSERT INTO tasks (title, done) VALUES (?, ?)", 
                       [
            ("Learn FastAPI",0),
            ("Build CRUD API",0),
            ("Read Assignment",1)
        ])
    conn.commit()

@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks")
def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    return [{"id": row[0], 
             "title": row[1], 
             "done": bool(row[2])} 
             for row in rows]

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()
    if row:
        return {"id": row[0], "title": row[1], "done": bool(row[2])}
    else:
        raise HTTPException(status_code=404, detail="Task not found")

from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str

@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    if not task.title.strip():
        raise HTTPException(status_code=400, detail="Title cannot be empty")
    
    task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "done": False
    }

    cursor.execute("INSERT INTO tasks (title, done) VALUES (?, ?)", 
                   (task.title, False))
    conn.commit()
    new_id = cursor.lastrowid
    return {
        "id": new_id,
        "title": task.title,
        "done": False
    }

class TaskUpdate(BaseModel):
    title: str
    done: bool

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    cursor.execute("Update tasks SET title = ?, done = ? WHERE id = ?", 
                   (task.title, task.done, task_id))
    conn.commit()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task not found")

    return {
        "id": task_id,
        "title": task.title,
        "done": task.done
    }

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))    
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task not found")
