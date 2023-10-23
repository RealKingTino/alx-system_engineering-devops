#!/usr/bin/python3
"""Exports data to CSV format for a given employee ID."""
import sys
import requests
import csv

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    with open('{}.csv'.format(employee_id), 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in todos:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': user.get('username'),
                'TASK_COMPLETED_STATUS': str(task.get('completed')),
                'TASK_TITLE': task.get('title')
            })
