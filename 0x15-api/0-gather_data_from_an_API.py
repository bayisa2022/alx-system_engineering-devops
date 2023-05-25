#!/usr/bin/python3
import requests
import json

def get_employee_todo_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    todos = json.loads(response.text)
    completed_todos = [todo for todo in todos if todo["completed"]]
    total_todos = len(todos)
    completed_todos_count = len(completed_todos)
    progress = (completed_todos_count / total_todos) * 100
    return f"Employee {employee_id} has completed {progress:.2f}% of their TODO list."

print(get_employee_todo_progress(1))
