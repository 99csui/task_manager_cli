from dataclasses import dataclass

from models.enums import TaskPriority, TaskStatus


@dataclass
class Task:
    id: int
    title: str
    description: str
    status: TaskStatus = TaskStatus.WAITING
    priority: TaskPriority = TaskPriority.MEDIUM

    def __post_init__(self):
        self._validate_id()
        self._validate_title()
        self._validate_description()
        self._validate_status(self.status)
        self._validate_priority(self.priority)


    def change_status(self, new_status: TaskStatus) -> None:
        self._validate_status(new_status)
        self.status = new_status
        


    def change_priority(self,new_priority: TaskPriority) -> None:
        self._validate_priority(new_priority)
        self.priority = new_priority
        


    def mark_as_finished(self) -> None:
        self.change_status(TaskStatus.FINISHED)

    def __str__(self):
       return (f"Taks ID: {self.id}\n"
                       f"Title: {self.title}\n"
                       f"Description: {self.description}\n"
                       f"Status: {self.status.value}\n"
                       f"Priority: {self.priority.value}")


    def _validate_id(self) -> None:
        if not isinstance(self.id,int):
            raise TypeError("the id must be an int")
        
        if self.id < 1:
            raise ValueError("id cannot be 0 or below")



    def _validate_title(self) -> None:
        if not isinstance(self.title,str):
            raise TypeError("the title must be a string")
        
        if self.title.strip() == "":
            raise ValueError("title cannot be empty")


    def _validate_description(self) -> None:
        if not isinstance(self.description,str):
            raise TypeError("the description must be a string")
        
        if self.description.strip() == "":
            raise ValueError("description cannot be empty")


    def _validate_status(self, status: TaskStatus) -> None:
        if not isinstance(status, TaskStatus):
            raise TypeError("status must be a TaskStatus")


    def _validate_priority(self, priority: TaskPriority) -> None:
        if not isinstance(priority, TaskPriority):
            raise TypeError("priority must be a TaskPriority")


    
    