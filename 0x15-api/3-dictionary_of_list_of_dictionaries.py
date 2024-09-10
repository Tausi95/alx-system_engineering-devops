#!/usr/bin/python3
"""from task #0, extending the Python script
to export data in the JSON format for all todos of all users.
"""

import json
import requests

if __name__ == "__main__":
    file_name = "todo_all_employees.json"
    API = "https://jsonplaceholder.typicode.com"
    my_dict = {}

    users = requests.get(API + "/users").json()
    for user in users:
        user_id = user.get("id")
        user_name = user.get("username")
        my_dict[user_id] = []
        user_todos = requests.get(API + "/users/{}/todos"
                                  .format(user_id)).json()

        for todo in user_todos:
            todo_dict = {
                "username": user_name,
                "task": todo.get('title'),
                "completed": todo.get('completed')
            }
            my_dict[user_id].append(todo_dict)

    with open(file_name, "w") as f:
        f.write(json.dumps(my_dict))
