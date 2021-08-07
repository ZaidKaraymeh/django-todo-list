from .views import home, newProject, newTask, task
from django.urls import path

urlpatterns = [
    path("", home, name="todo-home"),
    path("<str:projectTitle>/newtask/", newTask, name="todo-newTask"),
    path("newProject/", newProject, name="todo-newProject"),
    path("task/<int:id>/", task, name="todo-task"),
]