from models.task import Task

class TaskRepository:

    def __init__(self):
        self.tasks = []


    def add_task(self, task):
        if isinstance(task, Task):
            found_task = self.find_task_by_id(task.id)
            if found_task is not None:
                return False
            
            self.tasks.append(task)
            return True
        return False


    def find_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def list_tasks(self):
        return self.tasks

    def remove_task(self, task_id):
        found_task = self.find_task_by_id(task_id)
        if found_task is not None:
            self.tasks.remove(found_task)
            return True
        else:
            return False
