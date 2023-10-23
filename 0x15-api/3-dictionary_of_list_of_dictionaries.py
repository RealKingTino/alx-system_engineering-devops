#!/usr/bin/python3
"""Exports data to JSON format for all employees."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    all_data = {}

    for user in users:
        employee_id = str(user.get("id"))
        todos_url = url + "todos"
        params = {"userId": employee_id}
        todos = requests.get(todos_url, params=params).json()
        all_data[employee_id] = []
        for task in todos:
            all_data[employee_id].append({
                "username": user.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed")
            })

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(all_data, jsonfile)
