from models.task import Task
from models.enums import TaskPriority, TaskStatus


class TaskRepository:

    def __init__(self) -> None:
        self.tasks = []


    def add_task(self, task: Task) -> bool:
        if not isinstance(task, Task):
            return False
        
        found_task = self.find_task_by_id(task.id)
        if found_task is not None:
            return False
            
        self.tasks.append(task)
        return True
      


    def find_task_by_id(self, task_id: int) -> Task | None:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def list_tasks(self) -> list[Task]:
        return self.tasks.copy()

    def remove_task(self, task_id: int) -> bool:
        found_task = self.find_task_by_id(task_id)
        if found_task is None:
            return False
        
        self.tasks.remove(found_task)
        return True


    def change_task_status(self, task_id: int, new_status: TaskStatus) -> bool:
        found_task = self.find_task_by_id(task_id)
        if found_task is None:
            return False
        found_task.change_status(new_status)
        return True


    def change_task_priority(self, task_id: int, new_priority: TaskPriority) -> bool:
        found_task = self.find_task_by_id(task_id)
        if found_task is None:
            return False
        found_task.change_priority(new_priority)
        return True


