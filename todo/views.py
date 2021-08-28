from .models import Project, Task
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import NewProjectForm, NewTaskForm
from django.contrib import messages
from django.contrib.auth.models import User

import json

def home(request):
    context = {}
    if request.user.is_authenticated:
        author = request.user
        tasksNotCleaned = Task.objects.filter(author=author)

        tasks = [{"task_title": x[2], "id": x[0],} for x in tasksNotCleaned.values_list()]

        print("Project Titles: " ,[x for x in tasks])
        print(request.user.id)
        user = User.objects.get(username=f"{request.user}")
        projectsNotCleaned = user.project_set.all()
        print(projectsNotCleaned)
        projects =   [{
            "title": x[2], 
            "id": x[0], 
            "tasks":
            list(Task.objects.filter(project__project_title = x[2])) 
        
        }for x in projectsNotCleaned.values_list()]
        # Task.objects.filter(project__project_title= "iPhone 12").count()

        print("Projects: ", projectsNotCleaned.values())
        print("Tasks: ", tasksNotCleaned.values())
        context = {"projects":projects, "projectCount": projectsNotCleaned.count()}
    
    return render(request, "todo/home.html", context)

def task(request,  projectTitle, id):

    obj = Task.objects.filter(id=id).first()
    if request.method == "POST":
        form = NewTaskForm(request.POST or None, instance=obj)

        if form.is_valid():
            form.save(commit=False)
            form.save()
            messages.success(request, "Task Edited Successfully!")
            return redirect("todo-task", projectTitle=projectTitle, id=obj.id)
    else:
        form = NewTaskForm(instance=obj)
   


    tasks = Task.objects.filter(project__project_title=projectTitle)

    task = Task.objects.filter(id=id)
    task = task.first()
    
    
    context = {"tasks":tasks, "form":form, "title":projectTitle, "task":task, "id":id}
    return render(request, "todo/task.html", context)


def newTask(request, projectTitle):
    print("POST: ", request.POST)
    if request.method == "POST":
        form = NewTaskForm(request.POST or None)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            print(projectTitle)

            project_obj = Project.objects.filter(project_title = projectTitle).first()

            task.project = project_obj
            form.save()
            # done = form.cleaned_data.get("task_done")
            messages.success(request, "Task Posted!")
            return redirect("todo-task", projectTitle=projectTitle, id=task.id)
        
    else:
        form = NewTaskForm()

    tasks = Task.objects.filter(project__project_title=projectTitle)

    context=  {"form": form, "tasks":tasks, "title":projectTitle} 
    return render(request, "todo/newTask.html", context)




def newProject(request):
    print("POST: ", request.POST)
    if request.method == "POST":
        form = NewProjectForm(request.POST or None)
        print("Working")
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            form.save()
            # done = form.cleaned_data.get("task_done")
            messages.success(request, "Project Created Successfully!")
            return redirect("todo-home")
        
    else:
        form = NewProjectForm()
    context=  {"form": form} 
    return render(request, "todo/newProject.html", context)


# def editTask(request, id):
#     obj = Task.objects.filter(id=id).first()
#     if request.method == "PUT":
#         form = NewTaskForm(request.PUT or None, instance=obj)

#         if form.is_valid():
#             form.save(commit=False)
#             form.save()
#             messages.success(request, "Poem Edited!")
#             return redirect("blog-poem", id=obj.id)
#     else:
#         form = NewTaskForm(instance=obj)

#     return redirect("todo-task", projectTitle=obj.project, id=id)

def deleteTask(request, id):
    obj = Task.objects.filter(id=id)
    obj.delete()
    return redirect("todo-home")

def deleteProject(request, projectTitle):
    tasks = Task.objects.filter(project_project_title=projectTitle)
    tasks.delete()
    project = Project.objects.filter(project_title=projectTitle)
    return redirect("todo-home")

    