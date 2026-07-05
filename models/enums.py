from enum import Enum


class TaskStatus(str, Enum):
    
    WAITING = "waiting"
    
    IN_PROGRESS = "in_progress"

    FINISHED = "finished"


class TaskPriority(str, Enum):

    HIGH = "high"
    
    MEDIUM = "medium"

    LOW = "low"