# controller.py
class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    def add_task(self, task):
        self.model.add_task(task)
        self.update_view()
    def update_view(self):
        tasks = self.model.get_tasks()
        self.view.display_tasks(tasks)






