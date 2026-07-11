# Task Manager CLI


## Project Status

Current Version: v1.0

Status:

✔ Completed

The project has reached its first stable version and fulfills all planned functional requirements defined in the project plan.


## Overview

Task Manager CLI is a command-line application developed in Python that allows users to manage personal tasks through a simple console interface.

The project was built following software engineering best practices, including domain validation, the Repository Pattern, separation of responsibilities, clean architecture principles, and unit testing.


## Features

The application allows users to:

* Create new tasks.
* List all existing tasks.
* Search for a task by its ID.
* Remove tasks.
* Change the status of a task.
* Change the priority of a task.
* Validate user input before processing requests.
* Protect domain rules through entity validation.


## Software Engineering Principles

This project was developed following the following principles:

* Single Responsibility Principle (SRP)
* DRY (Don't Repeat Yourself)
* Fail Fast
* Separation of Concerns
* Repository Pattern
* Domain Validation


## Architecture

```text
task_manager_cli/
│
├── cli/
│   ├── __init__.py
│   └── menu.py
│
├── models/
│   ├── __init__.py
│   ├── enums.py
│   └── task.py
│
├── repositories/
│   ├── __init__.py
│   └── task_repository.py
│
├── tests/
│   ├── test_task.py
│   └── test_task_repository.py
│
├── main.py
├── README.md
└── PROJECT_PLAN.md
```


## Project Structure

```text
task_manager_cli/ 
│ 
├── cli/ 
│   ├── __init__.py  
|   └── menu.py # Console user interface 
│ 
├── models/ 
│   ├── __init__.py 
│   ├── enums.py # Domain enumerations 
│   └── task.py # Task entity 
│ 
├── repositories/ 
│ 
├── __init__.py 
│   └── task_repository.py # In-memory task repository 
│ 
├── tests/ 
│   ├── test_task.py 
│   └── test_task_repository.py 
│ 
├── main.py 
├── PROJECT_PLAN.md 
└── README.md
```


## Technologies

* Python 3
* unittest
* dataclasses
* Python Enum
* Git
* Command-Line Interface (CLI)


## Design Decisions

* Domain validation is handled by the Task entity.
* The repository is responsible for storing and retrieving tasks.
* The CLI layer is responsible only for user interaction.
* Business rules are separated from the presentation layer.


## Installation

Clone the repository:

```bash
git clone git@github.com:99csui/task_manager_cli.git
```

Move into the project directory:

```bash
cd task_manager_cli
```

(Optional) Create and activate a virtual environment.

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```


## Running the Application

Run the application with:

```bash
python main.py
```

The application will display the interactive console menu where tasks can be created, searched, updated, listed, and removed.


## Running the Tests

Run all unit tests with:

```bash
python -m unittest discover -s tests -v
```

All tests should pass successfully before creating a Pull Request or merging changes into the main branch.


## Example Usage

==== Task Manager ====

1. List tasks
2. Add task
3. Find task
4. Remove task
5. Change task status
6. Change task priority
0. Exit

Select an option:
2

* Id: 1
* Title: Study Python
* Description: Practice object-oriented programming

Task added successfully.


## Learning Objectives

This project was designed to practice and reinforce fundamental software engineering concepts, including:

* Object-Oriented Programming (OOP)
* Domain-driven design fundamentals
* Repository Pattern
* Separation of responsibilities
* Data validation
* Type hints
* Python dataclasses
* Enumerations
* Clean Code principles
* Unit testing with unittest
* Git workflow using feature branches
* Command-Line Interface (CLI) development


## Future Improvements

Possible future enhancements include:

* Add persistent storage using SQLite.
* Add automated CLI tests using mocks.
* Replace the generic user input validator with specialized input readers.
* Allow editing existing tasks.
* Add filtering and sorting options.
* Export tasks to JSON.
* Import tasks from JSON.
* Improve the console interface with colors and formatted tables.


## License

This project is licensed under the MIT License.

