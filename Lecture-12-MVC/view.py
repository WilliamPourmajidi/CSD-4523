#view.py
class TaskView:
    def display_tasks(self, tasks):
        print("Hey! This message comes from view.py. Here are the tasks:")
        for task in tasks:
            print(f"- {task}")








