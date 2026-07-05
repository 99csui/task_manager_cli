# Project Plan - Task Manager CLI

## 1. Project Vision

### Purpose

Task Manager CLI is a command-line application developed to practice professional software development using Python.

The project focuses on applying Object-Oriented Programming, software architecture, unit testing, Git workflow, and clean code principles while building a real portfolio project.

### Problem Statement

Users often need a simple way to organize and manage personal tasks.

The application will provide a clean and maintainable solution that allows users to create, update, organize and complete tasks from the command line.

### Success Criteria

The project will be considered successful when:

* All planned features are implemented.
* The application follows the selected architecture.
* Every public method is covered by unit tests.
* The Git history is clean and meaningful.
* The project documentation is complete.
* The project is suitable to be included in a professional portfolio.

---

# 2. Business Requirements

The system must allow users to:

* Create tasks.
* Search tasks by ID.
* List all tasks.
* Change task priority.
* Change task status.
* Mark tasks as completed.
* Remove tasks.

---

# 3. Functional Requirements

Version 1 must implement the following features:

### Task Management

* Create a new task.
* Remove an existing task.
* Find a task by its ID.
* List all tasks.

### Task Operations

* Change task status.
* Change task priority.
* Mark a task as finished.

---

# 4. Non-Functional Requirements

The project must:

* Be implemented using Object-Oriented Programming.
* Follow a layered architecture.
* Be fully tested using `unittest`.
* Follow PEP 8 conventions.
* Use meaningful names for classes, methods and variables.
* Keep responsibilities separated between layers.
* Use Git with feature branches.
* Follow Conventional Commits.

---

# 5. Project Scope

## Included

Version 1 includes:

* In-memory task storage.
* Command-line execution.
* Unit testing.
* Layered architecture.
* Professional Git workflow.

## Excluded

The following features are intentionally postponed:

* JSON persistence.
* Database support.
* REST API.
* Authentication.
* Multiple users.
* Graphical User Interface.
* Docker.
* Logging.
* Configuration files.

These features may be implemented in future versions.

---

# 6. Architecture

This project follows a simplified layered architecture.

```text
Presentation Layer (main.py)

        │

        ▼

Repository Layer

        │

        ▼

Domain Model
```

## Project Structure

```text
task_manager_cli/
│
├── models/
│   ├── task.py
│   └── enums.py
│
├── repositories/
│   └── task_repository.py
│
├── tests/
│   ├── test_task.py
│   └── test_task_repository.py
│
├── main.py
├── README.md
├── PROJECT_PLAN.md
└── .gitignore
```

---

# 7. Domain Model

## Task

### Responsibilities

* Represent a task.
* Change its own status.
* Change its own priority.
* Mark itself as finished.

### Attributes

* id
* title
* description
* status
* priority

### Public Methods

* change_status()
* change_priority()
* mark_as_finished()
* **str**()
* **eq**()

---

## TaskStatus

Allowed values:

* WAITING
* IN_PROGRESS
* FINISHED

---

## TaskPriority

Allowed values:

* LOW
* MEDIUM
* HIGH

---

# 8. Repository Layer

## TaskRepository

### Responsibilities

* Store tasks.
* Add tasks.
* Remove tasks.
* Search tasks by ID.
* List tasks.
* Update task status.
* Update task priority.

The repository is responsible only for managing the collection of tasks.

Business rules belong to the domain model.

---

# 9. Development Roadmap

## Sprint 0

* Project planning
* Git configuration
* Architecture
* Initial project structure

## Sprint 1

* Task model
* TaskStatus
* TaskPriority

## Sprint 2

* TaskRepository

## Sprint 3

* Task operations

## Sprint 4

* Unit testing

## Sprint 5

* Documentation

## Sprint 6

* Final code review
* Merge into main

---

# 10. Testing Strategy

The project will use Python's `unittest` framework.

Every public method must include tests covering:

* Successful execution.
* Invalid scenarios.
* Edge cases.

Tests should validate behavior instead of implementation details.

---

# 11. Git Workflow

## Branch Strategy

```text
main
│
└── feature/task_manager_cli
```

Development takes place in the feature branch.

The project is merged into `main` only after:

* All planned features are complete.
* All tests pass.
* Code review is completed.

## Commit Convention

The project follows Conventional Commits.

Examples:

* feat:
* fix:
* refactor:
* docs:
* test:
* chore:

Each commit should represent one logical unit of work.

---

# 12. Definition of Done

The project is considered complete when:

* All planned features are implemented.
* All unit tests pass.
* The architecture remains consistent.
* Code review is completed.
* Documentation is updated.
* Git history is clean.
* The README explains how to install, execute and test the application.

---

# 13. Future Improvements

Possible future versions may include:

* JSON persistence.
* SQLite support.
* PostgreSQL support.
* REST API with FastAPI.
* User authentication.
* Task categories.
* Due dates.
* Tags.
* Search filters.
* Docker support.
* Logging.
* Configuration management.
* Continuous Integration (CI).
