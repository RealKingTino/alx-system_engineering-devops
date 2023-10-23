#!/usr/bin/python3
"""Exports data to JSON format for a given employee ID."""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    data = {employee_id: []}
    for task in todos:
        data[employee_id].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        })

    with open('{}.json'.format(employee_id), 'w') as jsonfile:
        json.dump(data, jsonfile)
