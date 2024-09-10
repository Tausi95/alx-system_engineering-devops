#!/usr/bin/python3
"""From task #0, extend your Python script
to export data in the CSV format.
"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    try:
        user_id = argv[1]
        url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
        file_name = "{}.csv".format(user_id)
    except IndexError:
        exit

    res = requests.get(url)
    res = res.json()
    user_name = "{}".format(res.get('username'))
    res = requests.get(url + "/todos")
    res = res.json()

    with open(file_name, "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in res:
            writer.writerow([
                user_id,
                user_name,
                task.get('completed'),
                task.get('title')
            ])
