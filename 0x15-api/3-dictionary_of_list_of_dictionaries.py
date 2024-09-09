#!/usr/bin/python3
import json
import requests

# Define the URLs for fetching user and task data
users_url = "https://jsonplaceholder.typicode.com/users"
tasks_url = "https://jsonplaceholder.typicode.com/todos"

# Fetch user data and task data
users = requests.get(users_url).json()
tasks = requests.get(tasks_url).json()

# Create a dictionary to hold all tasks for all employees
all_tasks = {}

# Loop through each user to gather their tasks
for user in users:
    user_id = user['id']
    username = user['username']
    
    # Get all tasks for the current user
    user_tasks = []
    for task in tasks:
        if task['userId'] == user_id:
            user_tasks.append({
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            })
    
    # Add the tasks to the dictionary with the user ID as the key
    all_tasks[user_id] = user_tasks

# Write the dictionary to a JSON file
with open("todo_all_employees.json", "w") as json_file:
    json.dump(all_tasks, json_file)

