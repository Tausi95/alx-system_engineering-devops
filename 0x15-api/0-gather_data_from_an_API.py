#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user = requests.get(url).json()

    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos = requests.get(url).json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))

