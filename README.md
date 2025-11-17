# To-Do-list-python
Python project demonstrating CLI(Command line Interface) development, file handling and JSON -based task storage. Feature include add, view , and search tasks.
Project Overview

The To-Do List Manager is a Python-based application that allows users to efficiently manage their daily tasks. Tasks are saved permanently using JSON file storage, and users can add, view, and search tasks with priority and timestamp information.

Key Learning Outcomes:

File handling with JSON for persistent storage

Modular code design with reusable functions

Menu-driven CLI for user-friendly interaction

Handling date, time, and task priority

Basic searching and filtering of tasks

Features
Core Features

Add Task

Input task details including title, due date, due time, and priority.

Automatically stores the creation timestamp.

View Tasks

Display all tasks with numbering, due date, time, and priority.

Search Task

Search for tasks by keyword in the title (case-insensitive).

Persistent Storage

Stores tasks in tasks.json using structured JSON format.

Menu-Based Interaction

Easy-to-use CLI with options to add, view, search, or exit.

Requirements

Python 3.10+

No external libraries required (uses standard Python libraries: json, os, datetime)

How to Run

Save the project files in a folder, e.g., ToDoManager/.

Run the program:

python todo.py


Menu Options:

1 → Add Task

2 → View Tasks

3 → Search Task

4 → Exit

File Structure
ToDoManager/
├─ todo.py         # Main program
├─ tasks.json      # JSON file to store tasks (created automatically)
├─ README.md       # Project documentation

Author

Renu Joshi
