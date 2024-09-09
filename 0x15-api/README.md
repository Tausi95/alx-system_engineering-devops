# API 0x15 Project

This project focuses on interacting with RESTful APIs, fetching data, and exporting it into different formats using Python. Specifically, 
the project deals with fetching employee task completion data from a sample API and exporting this data in various formats like CSV, JSON, 
and even for multiple employees.

## Features

- **Task fetching**: Fetches data from a public API about employees and their tasks.
- **Single employee data export**: Exports task completion data for a single employee in either CSV or JSON format.
- **All employees data export**: Exports task data for all employees in JSON format.

## Project Directory Structure

- `0-gather_data_from_an_API.py` - Fetches and displays task data for a single employee from a RESTful API.
- `1-export_to_CSV.py` - Exports the task data of a single employee to a CSV file.
- `2-export_to_JSON.py` - Exports the task data of a single employee to a JSON file.
- `3-dictionary_of_list_of_dictionaries.py` - Exports the task data of all employees to a single JSON file.

## API Reference

The project interacts with the following endpoints from the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/):

- **Users**: `https://jsonplaceholder.typicode.com/users`  
  Retrieves user information like ID, username, and name.
  
- **Tasks**: `https://jsonplaceholder.typicode.com/todos`  
  Retrieves the to-do tasks for all employees, including task status (completed or not).

## Requirements

- Python 3.x
- `requests` library to handle API requests

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/api-0x15.git
   cd api-0x15
   ```

2. Install the required dependencies:

   ```bash
   pip install requests
   ```

## Usage

### 0-gather_data_from_an_API.py

Fetch the task completion data of an employee by passing their user ID as an argument:

```bash
python3 0-gather_data_from_an_API.py <employee_id>
```

### 1-export_to_CSV.py

Exports the tasks of an employee to a CSV file. The user ID must be provided as an argument:

```bash
python3 1-export_to_CSV.py <employee_id>
```

The output will be stored in a file named `<employee_id>.csv`.

### 2-export_to_JSON.py

Exports the tasks of an employee to a JSON file. Provide the employee ID as an argument:

```bash
python3 2-export_to_JSON.py <employee_id>
```

The output will be stored in a file named `<employee_id>.json`.

### 3-dictionary_of_list_of_dictionaries.py

Exports the tasks of all employees to a JSON file:

```bash
python3 3-dictionary_of_list_of_dictionaries.py
```

The output will be stored in `todo_all_employees.json`.

## Examples

### Example CSV Output:

For employee ID `1`, the CSV file will look like:

```csv
"USER_ID","USERNAME","TASK","COMPLETED"
1,"Bret","delectus aut autem","False"
1,"Bret","quis ut nam facilis et officia qui","True"
```

### Example JSON Output (Single Employee):

For employee ID `1`, the JSON output will be:

```json
{
    "1": [
        {
            "task": "delectus aut autem",
            "completed": false,
            "username": "Bret"
        },
        {
            "task": "quis ut nam facilis et officia qui",
            "completed": true,
            "username": "Bret"
        }
    ]
}
```

### Example JSON Output (All Employees):

```json
{
    "1": [
        {
            "username": "Bret",
            "task": "delectus aut autem",
            "completed": false
        }
    ],
    "2": [
        {
            "username": "Antonette",
            "task": "suscipit repellat esse quibusdam voluptatem incidunt",
            "completed": false
        }
    ]
}
```

## License

This project is licensed under the MIT License.
```
