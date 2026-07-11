from dataclasses import dataclass

from models.enums import TaskPriority, TaskStatus


@dataclass
class Task:
    id: int
    title: str
    description: str
    status: TaskStatus = TaskStatus.WAITING
    priority: TaskPriority = TaskPriority.MEDIUM

    def __post_init__(self) -> None:
        self._validate_id()
        self._validate_title()
        self._validate_description()
        self._validate_status(self.status)
        self._validate_priority(self.priority)


    def change_status(self, new_status: TaskStatus) -> None:
        self._validate_status(new_status)
        self.status = new_status
        


    def change_priority(self, new_priority: TaskPriority) -> None:
        self._validate_priority(new_priority)
        self.priority = new_priority
        


    def mark_as_finished(self) -> None:
        self.change_status(TaskStatus.FINISHED)

    def __str__(self) -> str:
       return (f"Task ID: {self.id}\n"
                       f"Title: {self.title}\n"
                       f"Description: {self.description}\n"
                       f"Status: {self.status.value}\n"
                       f"Priority: {self.priority.value}")


    def _validate_id(self) -> None:
        if not isinstance(self.id,int):
            raise TypeError("Id must be an integer")
        
        if self.id < 1:
            raise ValueError("Id must be greater than zero")



    def _validate_title(self) -> None:
        if not isinstance(self.title,str):
            raise TypeError("Title must be a string")
        
        if self.title.strip() == "":
            raise ValueError("Title cannot be empty")


    def _validate_description(self) -> None:
        if not isinstance(self.description,str):
            raise TypeError("Description must be a string")
        
        if self.description.strip() == "":
            raise ValueError("Description cannot be empty")


    def _validate_status(self, status: TaskStatus) -> None:
        if not isinstance(status, TaskStatus):
            raise TypeError("Status must be a TaskStatus")


    def _validate_priority(self, priority: TaskPriority) -> None:
        if not isinstance(priority, TaskPriority):
            raise TypeError("Priority must be a TaskPriority")


    
    