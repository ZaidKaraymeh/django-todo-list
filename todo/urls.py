from .views import home, newTask, task
from django.urls import path

urlpatterns = [
    path("", home, name="todo-home"),
    path("new/", newTask, name="todo-newTask"),
    path("task/<int:id>/", task, name="todo-task"),
]