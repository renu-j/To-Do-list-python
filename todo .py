# Todo project :
import json        # For reading and writing tasks in JSON format (permanent storage)
import os          # To check if the JSON file exists
from datetime import datetime  # To store the date and time when a task is added

# Path defined:
FILE = "tasks.json"  # The name of the file where all tasks will be saved

# function to load task:
def load_tasks():
    """
    Load tasks from the JSON file.
    Return an empty list if file doesn't exist or JSON is invalid/empty.
    """
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:  # If file is empty or invalid
            return []
    return []  # If file does not exist


# function to save task:
def save_tasks(tasks):
    """
    Save the current list of tasks to the JSON file.
    """
    with open(FILE, "w") as f:  # Open the file in write mode
        json.dump(tasks, f, indent=4)  # Convert Python list to JSON and save

# function to add task:
def add_task():
    """
    Add a new task with title, due date, time, priority, and created timestamp.
    """
    # Get task details from user
    title = input("Enter task name: ").strip()
    date = input("Enter due date (YYYY-MM-DD): ").strip()
    time = input("Enter due time (HH:MM): ").strip()
    priority = input("Priority (High/Medium/Low): ").strip().capitalize()

    # Create a dictionary for the task
    task = {
        "title": title,
        "date": date,
        "time": time,
        "priority": priority,
        "created": str(datetime.now())  # Store current date and time as string
    }

    # Load existing tasks, add the new task, then save all tasks
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!\n")

#function to view task:

def view_tasks():
    """
    Display all tasks stored in the JSON file.
    """
    tasks = load_tasks()  # Load tasks from JSON
    if not tasks:  # If list is empty
        print("No tasks found.\n")
        return

    # Print all tasks with numbering

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['title']} - {task['date']} {task['time']} | Priority: {task['priority']}")
    print()

# function to search task:
def search_task():
    """
    Search tasks by keyword in the task title.
    """
    keyword = input("Enter keyword to search: ").lower()  # Convert to lowercase for case-insensitive search
    tasks = load_tasks()  # Load tasks

    # Filter tasks that contain the keyword
    found = [t for t in tasks if keyword in t["title"].lower()]

    if not found:
        print("No task found.\n")
        return

    # Print found tasks
    print("\n--- SEARCH RESULTS ---")
    for task in found:
        print(f"{task['title']} - {task['date']} {task['time']} | Priority: {task['priority']}")
    print()

# Creating the main function that include teh menu for task:
def main():

    while True:
        print(" TO-DO LIST MENU ")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Search Task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        # Call functions based on user choice
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            search_task()
        elif choice == "4":
            print("Goodbye!")
            break  # Exit the loop and program
        else:
            print("Invalid choice. Try again.\n")  # Handle invalid input

# for run the program:
if __name__ == "__main__":
    main()
