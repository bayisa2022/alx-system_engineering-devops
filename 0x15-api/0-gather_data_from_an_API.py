import requests
import sys

# Define the base URL for the API
base_url = 'https://jsonplaceholder.typicode.com'

# Get the employee ID from the command line argument
employee_id = sys.argv[1]

# Make a GET request to retrieve the user information
user_response = requests.get(f'{base_url}/users/{employee_id}')
user_data = user_response.json()

# Make a GET request to retrieve the user's TODO list
todo_response = requests.get(f'{base_url}/todos?userId={employee_id}')
todo_data = todo_response.json()

# Count the number of completed tasks and total tasks
completed_tasks = [task for task in todo_data if task['completed']]
num_completed_tasks = len(completed_tasks)
total_tasks = len(todo_data)

# Display the employee TODO list progress
print(f"Employee {user_data['name']} is done with tasks({num_completed_tasks}/{total_tasks}):")

# Display the titles of completed tasks
for task in completed_tasks:
    print(f"\t {task['title']}")
