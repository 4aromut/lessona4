class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = "Not completed"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_completed(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                task.status = "Completed"
                break

    def show_current_tasks(self):
        current_tasks = [task for task in self.tasks if task.status == "Not completed"]
        if len(current_tasks) == 0:
            print("No current tasks")
        else:
            for task in current_tasks:
                print(f"Description: {task.description}, Deadline: {task.deadline}, Status: {task.status}")

# Пример использования
task_manager = TaskManager()


task1 = Task("Do laundry", "2022-01-20")
task2 = Task("Buy groceries", "2022-01-25")
task3 = Task("Finish project", "2022-02-10")

task_manager.add_task(task1)
task_manager.add_task(task2)
task_manager.add_task(task3)

task_manager.show_current_tasks()

task_manager.mark_task_completed("Do laundry")

task_manager.show_current_tasks()
