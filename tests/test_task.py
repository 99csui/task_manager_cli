import unittest

from models.enums import TaskPriority, TaskStatus
from models.task import Task

class TestTask(unittest.TestCase):

    def test_task_start_with_default_status(self):
        task = Task(1, "Study python", "Practice dataclasses")

        self.assertEqual(task.status, TaskStatus.WAITING)


    def test_task_starts_with_default_priority(self):
        task = Task(1, "Study Python", "Practice dataclasses")

        self.assertEqual(task.priority, TaskPriority.MEDIUM)



    def test_change_status_updates_status(self):
        task = Task(1, "Study Python", "Practice dataclasses")
        
        task.change_status(TaskStatus.IN_PROGRESS)

        self.assertEqual(task.status, TaskStatus.IN_PROGRESS)



    def test_change_priority_updates_priority(self):
        task = Task(1, "Study Python", "Practice dataclasses")
        
        task.change_priority(TaskPriority.HIGH)

        self.assertEqual(task.priority, TaskPriority.HIGH)



    def test_mark_as_finished_sets_status_to_finished(self):
        task = Task(1, "Study Python", "Practice dataclasses")
        
        task.mark_as_finished()

        self.assertEqual(task.status, TaskStatus.FINISHED)



