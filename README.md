# Project Management CLI Tool

## Overview

This is a Python Command-Line Interface (CLI) application that allows administrators to manage users, projects, and tasks.

The application stores data locally using JSON files and demonstrates Object-Oriented Programming (OOP), file handling, command-line argument parsing, automated testing, and modular project organization.

---

## Features

* Add new users
* View all users
* Add projects to users
* View projects for a specific user
* Add tasks to projects
* Mark tasks as completed
* Save and load data using JSON persistence
* Display users and projects using Rich tables
* Validate user and project data
* Unit tests using pytest

---

## Project Structure

```text
project-management-cli/
│
├── data/
│   └── data.json
│
├── models/
│   ├── person.py
│   ├── user.py
│   ├── project.py
│   ├── task.py
│   └── __init__.py
│
├── tests/
│   ├── test_person.py
│   ├── test_user.py
│   ├── test_project.py
│   └── test_task.py
│
├── utils/
│   ├── storage.py
│   ├── helpers.py
│   └── __init__.py
│
├── main.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python 3.12
* argparse (command-line argument parsing)
* JSON (data persistence)
* Rich (formatted terminal output)
* pytest (automated testing)

---

# Installation

## 1. Clone the repository

```bash
git clone <repository-url>
```

## 2. Navigate to the project folder

```bash
cd project-management-cli
```

## 3. Create a virtual environment

```bash
python -m venv .venv
```

## 4. Activate the virtual environment

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

## 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

The CLI uses `argparse` to provide multiple commands for managing users, projects, and tasks.

## Add a User

```bash
python main.py add-user --name "Alex" --email "alex@gmail.com"
```

## List Users

```bash
python main.py list-users
```

## Add a Project

```bash
python main.py add-project --user "Alex" --title "CLI Tool" --description "Python CLI project" --due-date "2026-08-01"
```

## List Projects

```bash
python main.py list-projects --user "Alex"
```

## Add a Task

```bash
python main.py add-task --user "Alex" --project "CLI Tool" --title "Implement add-task" --assigned-to "Alex"
```

## Complete a Task

```bash
python main.py complete-task --user "Alex" --project "CLI Tool" --title "Implement add-task"
```

---

# Application Flow

The application follows this object-oriented structure:

```
Person
  |
  |
User
  |
  |
Projects
  |
  |
Tasks
```

The CLI receives commands through `argparse`, updates the JSON data store, and displays information using Rich formatted tables.

---

# Object-Oriented Design

The project uses four main classes:

## Person

A base class containing shared user information such as name and email.

## User

Inherits from Person and manages projects.

## Project

Stores project details and contains related tasks.

## Task

Represents work assigned to a user and tracks completion status.

## Class Relationships

* One User can have many Projects.
* One Project can have many Tasks.
* Tasks belong to projects and represent individual pieces of work.

---

# Data Persistence

The application stores all information in:

```
data/data.json
```

The JSON file is automatically updated whenever users, projects, or tasks are added or modified.

The storage logic is separated into utility functions to keep file handling organized and reusable.

---

# Testing

The project uses **pytest** for automated testing.

Tests cover:

* Person validation
* User creation
* Unique user IDs
* User and project relationships
* Project and task relationships
* Task completion
* Object string representations

Run all tests:

```bash
python -m pytest
```

Run a single test file:

```bash
python -m pytest tests/test_person.py
```

Example successful output:

```
18 passed
```

---

# Known Limitations

* Data is stored locally and not in a database.
* Projects with the same name are not currently prevented.
* Users with duplicate names or emails can be added.
* Tasks cannot currently be deleted or edited.

---

# Future Improvements

* Add delete functionality for users, projects, and tasks.
* Edit existing records.
* Search for tasks.
* Filter completed tasks.
* Add task due dates.
* Add more detailed error messages and input validation.
* Add additional CLI tests using mock input.
* Store data using a database.

---

# Author

Irene

---

# License

This project was created for educational purposes.
