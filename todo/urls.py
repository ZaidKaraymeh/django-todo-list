from .views import deleteTask, home, newProject, newTask, task
from django.urls import path

urlpatterns = [
    path("", home, name="todo-home"),
    path("<str:projectTitle>/newtask/", newTask, name="todo-newTask"),
    path("<str:projectTitle>/task/<int:id>", task, name="todo-task"),
    path("task/<int:id>", deleteTask, name="todo-task-delete"),
    path("newProject/", newProject, name="todo-newProject"),
]