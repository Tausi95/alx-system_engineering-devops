#!/usr/bin/python3
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    task_list = []
    for task in todos:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        }
        task_list.append(task_dict)

    with open(f"{employee_id}.json", "w") as jsonfile:
        json.dump({employee_id: task_list}, jsonfile)

