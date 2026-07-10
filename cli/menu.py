from models.enums import TaskPriority, TaskStatus
from models.task import Task
from repositories.task_repository import TaskRepository


class ConsoleMenu:
    def __init__(self) -> None:
        self.repository = TaskRepository()


    def run(self) -> None:
        running = True
        while running:
            print(self._show_menu())
            option = input("Select an option\n").strip()
            if option == "0":
                running = False
                print("Goodbye!")

            elif option == "1":
                self._list_tasks()

            elif option == "2":
                self._add_task()
            
            elif option == "3":
                self._find_task()

            elif option == "4":
                self._remove_task()

            elif option == "5":
                self._change_status()

            elif option == "6":
                self._change_priority()

            else:
                print("Invalid option.\n")
        

    def _show_menu(self) -> str:
        menu = "==== Task Manager ====\n" \
        "1. List tasks\n" \
        "2. Add task\n" \
        "3. Find task\n" \
        "4. Remove task\n" \
        "5. Change task status\n" \
        "6. Change task priority\n" \
        "0. Exit"
        return menu

    def _list_tasks(self) -> None:
        tasks = self.repository.list_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            for task in tasks:
                print(task)
                print()



    def _add_task(self) -> None:
        print("***Add Task***")
        task_id = self._validate_user_input("int", "Id")
        title = self._validate_user_input("str", "Title")
        description = self._validate_user_input("str", "Description")
        try:
            task = Task(task_id,title,description)
            result = self.repository.add_task(task)
            if result:
                print("Task added successfully.")
            else:
                print("Task could not be added.")
        except (TypeError, ValueError) as error:
            print(error)

    def _find_task(self) -> None:
        print("**** Find task by id ****")
        task = self._get_task_from_user_input()
        if task is not None:
            print(f"Task with ID {task.id} found.")
            print(task)


    def _remove_task(self) -> None:
        print("**** Remove task ****")
        task_id = self._validate_user_input("int", "Id")
        result = self.repository.remove_task(task_id)
        if result:
            print(f"Task with ID {task_id} removed.")
        else:
            print(f"Task with ID {task_id} does not exist.")
                
    
    def _change_status(self) -> None:
        print("**** Change task status ****")
        print("Enter id to search task")
        task_found = self._get_task_from_user_input()
        if task_found is not None:
            print("Select new task status")        
            print(f"1. {TaskStatus.WAITING.value}   2. {TaskStatus.IN_PROGRESS.value}   3. {TaskStatus.FINISHED.value}")
            new_task_status = self._validate_user_input("TaskStatus", "Status")

            result = self.repository.change_task_status(task_found.id, new_task_status)
            if result:
                print("Task status updated successfully.")
            else:
                print("The task status cannot be changed.")
        

    def _change_priority(self) -> None:
        print("**** Change task priority ****")
        print("Enter id to search task")
        task_found = self._get_task_from_user_input()
        if task_found is not None:                    
            print("Select new task priority")        
            print(f"1. {TaskPriority.HIGH.value}\n"
                  f"2. {TaskPriority.MEDIUM.value}\n"
                  f"3. {TaskPriority.LOW.value}")
            new_task_priority = self._validate_user_input("TaskPriority", "Priority")

            result = self.repository.change_task_priority(task_found.id, new_task_priority)
            if result:
                print("Task priority updated successfully.")
            else:
                print("The task priority cannot be changed.")


    def _validate_user_input(self, type_input: str,input_user: str) -> int | str | TaskStatus | TaskPriority:
        while True:
            value = input(f"{input_user}: ")
            strip_value = value.strip()
            if not strip_value:
                print(f"{input_user} cannot be empty.")
                 
            else:
                if type_input == "str":
                    return strip_value
                
                elif type_input == "int":
                    try:
                        
                        number = int(strip_value)
                        if number < 1:
                            print(f"{input_user} cannot be 0 or below.")
                        else:
                            return number
                    except ValueError:
                        print(f"{input_user} it must be a number.")

                elif type_input == "TaskStatus":
                    if strip_value == "1":
                        return TaskStatus.WAITING
                    elif strip_value == "2":
                        return TaskStatus.IN_PROGRESS
                    elif strip_value == "3":
                        return TaskStatus.FINISHED
                    else:
                        print("Invalid option.")

                elif type_input == "TaskPriority":
                    if strip_value == "1":
                        return TaskPriority.HIGH
                    elif strip_value == "2":
                        return TaskPriority.MEDIUM
                    elif strip_value == "3":
                        return TaskPriority.LOW
                    else:
                        print("Invalid option.")


    def _get_task_from_user_input(self) -> Task | None:
        task_id = self._validate_user_input("int", "Id")
        task = self.repository.find_task_by_id(task_id)

        if task is None:
            print(f"Task with ID {task_id} does not exist.")

        return task
