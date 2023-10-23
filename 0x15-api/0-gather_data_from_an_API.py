#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
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

    completed_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
