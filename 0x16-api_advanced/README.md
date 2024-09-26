
# Reddit API Advanced

This project involves interacting with the Reddit API to query information about hot articles in subreddits. The focus is on implementing recursive functions to handle API data efficiently and meeting specific query requirements such as counting keyword occurrences and printing data in a sorted format.

## Table of Contents
- [Introduction](#introduction)
- [Learning Objectives](#learning-objectives)
- [Project Requirements](#project-requirements)
- [Tasks Overview](#tasks-overview)
  - [Task 0: How many subs?](#task-0-how-many-subs)
  - [Task 1: Top Ten](#task-1-top-ten)
  - [Task 2: Recurse it!](#task-2-recurse-it)
  - [Task 3: Count it!](#task-3-count-it)
- [Example Usage](#example-usage)
- [Notes and Edge Cases](#notes-and-edge-cases)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction

In this project, you will implement several Python functions that interact with the Reddit API, allowing you to:
- Query information about subreddits.
- Retrieve hot articles.
- Count keyword occurrences in post titles.
  
The tasks will focus on both efficient data retrieval and recursive implementation, avoiding the use of loops.

## Learning Objectives

By completing this project, you should be able to:
- Query RESTful APIs.
- Use recursive functions for data processing.
- Handle pagination with APIs.
- Parse and manipulate data from JSON responses.

## Project Requirements

- Language: Python 3.8+
- Libraries: `requests` for API interaction
- User-Agent: Use a custom User-Agent string for API requests to avoid being blocked by Reddit.

## Tasks Overview

### Task 0: How many subs?

Prototype: `def number_of_subscribers(subreddit)`

This function queries the Reddit API and returns the number of subscribers for a given subreddit.

#### Example:
```bash
$ python3 0-main.py programming
756024
```

If the subreddit is invalid or doesn't exist, it returns `0`.

---

### Task 1: Top Ten

Prototype: `def top_ten(subreddit)`

This function queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

- Titles should be printed in order from the hottest to the least hot.
- If the subreddit is invalid, print `None`.

#### Example:
```bash
$ python3 1-main.py programming
Understanding Recursion
Python tips and tricks
How to write a recursive function in Python
...
```

---

### Task 2: Recurse it!

Prototype: `def recurse(subreddit, hot_list=[])`

This recursive function queries the Reddit API and returns a list of all hot post titles for a given subreddit.

- If no results are found for the given subreddit, return `None`.
- The function should handle pagination by recursively querying using the `after` parameter.

#### Example:
```bash
$ python3 2-main.py programming
['Understanding Recursion', 'Python tips and tricks', 'How to write a recursive function in Python', ...]
```

---

### Task 3: Count it!

Prototype: `def count_words(subreddit, word_list)`

This recursive function queries the Reddit API, parses the titles of hot articles, and prints a sorted count of given keywords (case-insensitive).

- The count should be printed in descending order by occurrences.
- If two words have the same count, they should be sorted alphabetically.
- Words that don't appear in any titles should be skipped.

#### Example:
```bash
$ python3 100-main.py programming 'python java javascript scala no_results_for_this_one'
java: 27
javascript: 20
python: 17
scala: 4

$ python3 100-main.py programming 'JavA java'
java: 54
```

---

## Example Usage

Here are some example commands you can use to test the functionality of the various tasks:

### Task 0 Example:
```bash
$ python3 0-main.py programming
756024
```

### Task 1 Example:
```bash
$ python3 1-main.py programming
Understanding Recursion
Python tips and tricks
How to write a recursive function in Python
...
```

### Task 2 Example:
```bash
$ python3 2-main.py programming
['Understanding Recursion', 'Python tips and tricks', 'How to write a recursive function in Python', ...]
```

### Task 3 Example:
```bash
$ python3 100-main.py programming 'react python java javascript scala'
java: 27
javascript: 20
python: 17
react: 17
scala: 4
```

---

## Notes and Edge Cases

1. API Limit*:
   - Reddit imposes rate limits on API requests. If you're testing frequently, be mindful of these limits.

2. Invalid Subreddits:
   - If the subreddit is invalid, ensure that no redirects are followed and that the function returns `0` or `None` as appropriate.

3. Case-Insensitive Matching:
   - All keyword matching is case-insensitive. Ensure both the subreddit titles and the keywords are converted to lowercase during processing.

4. Recursive Functions:
   - Be cautious of infinite recursion or hitting recursion limits when testing with large datasets.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Tausi95/alx-system_engineering-devops.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd alx-system_engineering-devops/0x16-api_advanced
   ```

3. Install the required dependencies:
   ```bash
   pip install requests
   ```

---

## Usage

To run each task, use the provided `main.py` files:

```bash
python3 0-main.py <subreddit_name>
python3 1-main.py <subreddit_name>
python3 2-main.py <subreddit_name>
python3 100-main.py <subreddit_name> '<list of keywords>'
```

---

## License

