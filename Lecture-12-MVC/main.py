# main.py
from model import TaskModel
from view import TaskView
from controller import TaskController

# Create instances of Model, View, and Controller
model = TaskModel()
view = TaskView()
controller = TaskController(model, view)
# Add tasks using the Controller


while True:
    inp = input('Enter a task: ')
    controller.add_task(inp)
