# model.py
class TaskModel:
    def __init__(self):
        self.tasks = []

    # Setter Method!
    def add_task(self, task):
        self.tasks.append(task)

    # Getter Method!
    def get_tasks(self):
        return self.tasks
