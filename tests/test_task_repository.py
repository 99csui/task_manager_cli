import unittest

from models.task import Task
from repositories.task_repository import TaskRepository


class TestTaskRepository(unittest.TestCase):

    def test_repository_starts_with_empty_tasks(self):
        repository = TaskRepository()

        self.assertEqual(repository.tasks,[])


    def test_add_task_adds_valid_task(self):
        task = Task(1,"Study Python","Study with the intention of getting a job")
        repository = TaskRepository()

        repository.add_task(task)
        result = repository.tasks[0]
        self.assertEqual(result,task)


    def test_add_task_returns_false_for_invalid_object(self):
        task = "this is a test"
        repository = TaskRepository()

        result = repository.add_task(task)
        self.assertFalse(result)


    def test_add_task_returns_false_for_duplicate_id(self):
        task = Task(1,"Study Python","Study with the intention of getting a job")
        repository = TaskRepository()

        repository.add_task(task)
        result = repository.add_task(task)
        self.assertFalse(result)


    def test_find_task_by_id_returns_task_when_exists(self):
        task = Task(1,"Study Python","Study with the intention of getting a job")
        repository = TaskRepository()

        repository.add_task(task)
        result = repository.find_task_by_id(task.id)
        self.assertEqual(result,task)


    def test_find_task_by_id_returns_none_when_task_does_not_exist(self):
        task = Task(1,"Study Python","Study with the intention of getting a job")
        repository = TaskRepository()

        repository.add_task(task)
        result = repository.find_task_by_id(2)
        
        self.assertIsNone(result)


    def test_list_tasks_returns_all_tasks(self):
        task = Task(1,"Study Python","Study with the intention of getting a job")
        repository = TaskRepository()

        repository.add_task(task)
        result = repository.list_tasks()
    
        self.assertIn(task,result)



    def test_remove_task_returns_true_when_task_exists(self):
        task = Task(1,"Study Python","Study with the intention of getting a job")
        repository = TaskRepository()

        repository.add_task(task)
        result = repository.remove_task(task.id)
        self.assertTrue(result)


    def test_remove_task_removes_task_from_repository(self):
        task = Task(1,"Study Python","Study with the intention of getting a job")
        repository = TaskRepository()

        repository.add_task(task)
        repository.remove_task(task.id)
        result = repository.find_task_by_id(task.id)        
        self.assertIsNone(result)




    def test_remove_task_returns_false_when_task_does_not_exist(self):
        task = Task(1,"Study Python","Study with the intention of getting a job")
        repository = TaskRepository()

        repository.add_task(task)
        result = repository.remove_task(2)
        self.assertFalse(result)











