# To-Do List Project

# Overview
This is a simple Python project to manage daily tasks using JSON-based storage. The program allows users to **add, view, and search tasks**, each with a due date, time, and priority. All tasks are stored permanently in a JSON file (`tasks.json`), and each task includes a creation timestamp. The project provides a **clean command-line interface** and demonstrates basic Python programming, file handling, and data management.

---

# Features
- Add tasks with title, due date, time, and priority (High/Medium/Low)
- View all stored tasks in a numbered list
- Search tasks by keyword in the task title
- Persistent storage using JSON
- Task creation timestamp
- Interactive command-line menu

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/renu-j/To-Do-python.git

2.Navigate to the project directory
-cd todo-list

3.Run the progarm
-python main.py

## Usage
1.Add Task: Enter task details (title, due date, time, priority) when prompted.
2.View Tasks: Displays all tasks with due dates, times, and priority levels.
3.Search Task: Search tasks by typing a keyword from the task title.
4.Exit: Quit the program.

## file Structure
todo-list/
├── todo.py         # Main Python program with all task functions
├── tasks.json      # JSON file storing tasks
├── README.md       # Project description
└── .gitignore      # Optional: files to ignore in Git

## Author
-Renu Joshi
