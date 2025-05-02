import sqlite3
from datetime import datetime

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    due_date TEXT,
    completed INTEGER DEFAULT 0
                )
""")

conn.commit()

def add_task(title, due_date):
    cursor.execute("INSERT INTO tasks (title, due_date) VALUES (?,?)",(title,due_date))
    conn.commit()
    print("Task added. \n")


def view_tasks(only_pending=False):
    # choose the query based on whether we want only peding taks
    if only_pending:
        cursor.execute("SELECT id, title, due_date, completed FROM tasks where completed = 0")
    else:
        cursor.execute("SELECT id, title, due_date, completed from tasks")

    tasks = cursor.fetchall()

    # show a message if no tasks are found
    if not tasks:
        print("No tasks found. \n")
        return
    
    # print each task
    for task in tasks:
        task_id, title, due_date, completed = task
        status = "Done" if completed else "Pending"
        print(f"{task_id}. {title} (Due: {due_date}) - {status}")
    print()



def mark_complete(task_id):
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id))
    conn.commit()
    print("Tasks marked as complete. \n")


def delete_task(task_id):
    cursor.execute("DELETE FROM tasks where id = ?", (task_id))
    conn.commit()
    print("Task deleted. \n")

def close_connection():
    conn.close()

    
     


