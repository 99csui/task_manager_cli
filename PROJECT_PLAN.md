# Project Plan – Task Manager CLI

## 1. Project Overview

### Project Name

Task Manager CLI

### Description

Task Manager CLI is a command-line application developed in Python that allows users to manage personal tasks through a simple and intuitive interface.

The main objective of this project is to practice software engineering fundamentals while building a clean, maintainable, and well-tested Python application.

This project follows a layered architecture separating:

* Domain Model
* Repository Layer
* Console User Interface

---

# 2. Learning Objectives

This project focuses on practicing:

* Python fundamentals
* Object-Oriented Programming
* Dataclasses
* Enumerations
* Type Hints
* Clean Code
* Repository Pattern
* Domain Validation
* Separation of Responsibilities
* Unit Testing with unittest
* Git workflow
* Command Line Interfaces (CLI)

---

# 3. Business Requirements

The application must allow the user to:

* Create tasks.
* List all tasks.
* Search a task by ID.
* Remove tasks.
* Change task status (including marking a task as finished).
* Change task priority.

---

# 4. Functional Requirements

Each task must contain:

* ID
* Title
* Description
* Status
* Priority

Rules:

* Task IDs must be unique.
* IDs must be greater than zero.
* Title cannot be empty.
* Description cannot be empty.
* Status must be a valid TaskStatus.
* Priority must be a valid TaskPriority.

---

# 5. Architecture

```text
main.py
        │
        ▼
ConsoleMenu
        │
        ▼
TaskRepository
        │
        ▼
Task
```

Responsibilities:

## Task

Responsible for:

* Representing a task.
* Protecting domain invariants.
* Validating its own data.
* Changing its own state.

## TaskRepository

Responsible for:

* Storing tasks.
* Searching tasks.
* Removing tasks.
* Preventing duplicated IDs.
* Delegating modifications to Task.

## ConsoleMenu

Responsible for:

* Interacting with the user.
* Reading input.
* Displaying information.
* Calling the repository.

---

# 6. Project Structure

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

---

# 7. Coding Standards

The project follows:

* PEP 8
* Type Hints
* Fail Fast
* DRY (Don't Repeat Yourself)
* Single Responsibility Principle
* Clear and descriptive names
* Small methods with a single responsibility

---

# 8. Git Workflow

Development is performed using feature branches.

Workflow:

```text
main
    │
    └── feature/<feature-name>
```

Each feature should be developed independently and merged into `main` through a Pull Request after review.

Commit messages should follow a clear convention, for example:

```text
feat: add task validation
fix: correct duplicate id validation
refactor: simplify repository methods
test: add repository unit tests
docs: update project documentation
```

---

# 9. Testing Strategy

The project uses Python's `unittest` framework.

Unit tests cover the domain and repository layers.

Tests include:

* Successful scenarios.
* Invalid input.
* Edge cases.
* Domain validation.

The console interface is verified through manual acceptance testing.

Tests focus on validating behavior rather than implementation details.

---

# 10. Development Roadmap

## Sprint 1

* Project setup
* Domain model
* Enums
* Dataclass

## Sprint 2

* Repository implementation
* Repository tests

## Sprint 3

* Domain validation
* Validation tests
* Type hints

## Sprint 4

* Console interface
* User input validation
* Manual acceptance testing

## Sprint 5

* Final code review
* Refactoring
* Documentation
* README

## Sprint 6

* Final Pull Request
* Merge into main
* Project release

---

# 11. Technical Debt

Known improvements for future versions:

* Replace the generic `_validate_user_input()` method with specialized input readers.
* Add automated tests for the CLI using mocks.
* Improve dependency injection for `ConsoleMenu`.
* Return copies of internal collections when appropriate.
* Add persistent storage (JSON or SQLite).
* Add filtering and sorting options.
* Improve user experience with richer console output.

---

# 12. Definition of Done

The project is considered complete when:

* All planned features are implemented.
* Domain and repository unit tests pass successfully.
* The console interface passes manual acceptance testing.
* The architecture remains clean and consistent.
* Code review findings have been addressed.
* Documentation is complete.
* Git history is clean.
* A professional README has been written.
* The project has been merged into `main`.
