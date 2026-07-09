from models.enums import TaskPriority, TaskStatus
from models.task import Task
from repositories.task_repository import TaskRepository


def main():
    repository = TaskRepository()

    task = Task(
        1,
        "Study Python",
        "Practice domain validation and repository pattern",
    )

    repository.add_task(task)

    print("All tasks:")
    for task in repository.list_tasks():
        print(task)

    repository.change_task_status(1, TaskStatus.IN_PROGRESS)
    repository.change_task_priority(1, TaskPriority.HIGH)

    print("Updated task:")
    print(repository.find_task_by_id(1))

    repository.remove_task(1)

    print("Tasks after removal:")
    print(repository.list_tasks())


if __name__ == "__main__":
    main()