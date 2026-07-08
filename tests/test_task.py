import unittest

from models.enums import TaskPriority, TaskStatus
from models.task import Task

class TestTask(unittest.TestCase):

    def test_task_start_with_default_status(self):
        task = Task(1, "Study Python", "Practice dataclasses")

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


    def test_task_raises_type_error_when_title_is_not_string(self):
        with self.assertRaises(TypeError):
            Task(1, 1, "Practice dataclasses")


    def test_task_raises_value_error_when_title_is_empty(self):
        with self.assertRaises(ValueError):
            task = Task(1, "", "Practice dataclasses")


    def test_task_raises_value_error_when_title_has_only_spaces(self):
        with self.assertRaises(ValueError):
            task = Task(1, "     ", "Practice dataclasses")


    def test_task_raises_type_error_when_status_is_invalid(self):
        with self.assertRaises(TypeError):
            task = Task(1, "Study Python", "Practice dataclasses", "banana")



    def test_task_raises_type_error_when_priority_is_invalid(self):
        with self.assertRaises(TypeError):
            task = Task(1, "Study Python", "Practice dataclasses", TaskStatus.IN_PROGRESS, "banana")


    def test_change_status_raises_type_error_when_status_is_invalid(self):
        task = Task(1, "Study Python", "Practice dataclasses")
        with self.assertRaises(TypeError):
            task.change_status("banana")


    def test_change_priority_raises_type_error_when_priority_is_invalid(self):
        task = Task(1, "Study Python", "Practice dataclasses")
        with self.assertRaises(TypeError):
            task.change_priority("banana")



