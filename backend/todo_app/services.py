import logging
logger = logging.getLogger(__name__)

from .db import get_connection

def fetch_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description, due_date, status FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    return rows


def insert_task(title, description, due_date, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description, due_date, status) VALUES (?, ?, ?, ?)",
        (title, description, due_date, status)
    )
    conn.commit()
    conn.close()


def update_task(task_id, title, description, due_date, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET title=?, description=?, due_date=?, status=? WHERE id=?",
        (title, description, due_date, status, task_id)
    )
    conn.commit()
    conn.close()


def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()


def fetch_task_by_id(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description, due_date, status FROM tasks WHERE id=?", (task_id,))
    row = cursor.fetchone()
    conn.close()
    return row
