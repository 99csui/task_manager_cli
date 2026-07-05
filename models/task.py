from dataclasses import dataclass

from models.enums import TaskPriority, TaskStatus


@dataclass
class Task:
    id: int
    title: str
    description: str
    status: TaskStatus = TaskStatus.WAITING
    priority: TaskPriority = TaskPriority.MEDIUM

    def change_status(self, new_status):
        self.status = new_status


    def change_priority(self,new_priority):
        self.priority = new_priority


    def mark_as_finished(self):
        self.change_status(TaskStatus.FINISHED)


