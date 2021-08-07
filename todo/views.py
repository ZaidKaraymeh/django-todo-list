from .models import Project, Task
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import NewProjectForm, NewTaskForm
from django.contrib import messages

# Create your views here.


def home(request):
    author = request.user
    tasksNotCleaned = Task.objects.filter(author=author)

    tasks = [{"task_title": x[2], "id": x[0],} for x in tasksNotCleaned.values_list()]

    print("Project Titles: " ,[x for x in tasks])

    projectsNotCleaned = Project.objects.all()
    projects =   [{
        "title": x[1], 
        "id": x[0], 
        "tasks":
        list(Task.objects.filter(project__project_title = x[1])) 
    
    }for x in projectsNotCleaned.values_list()]
    # Task.objects.filter(project__project_title= "iPhone 12").count()

    print("Projects: ", projectsNotCleaned.values_list())
    print("Tasks: ", tasksNotCleaned.values_list())
    print(projects[0])
    context = {"projects":projects}

    return render(request, "todo/home.html", context)

def task(request, id):

    obj = Task.objects.filter(id=id).first()
    if request.method == "POST":
        form = NewTaskForm(request.POST or None, instance=obj)

        if form.is_valid():
            form.save(commit=False)
            form.save()
            messages.success(request, "Task Edited Successfully!")
            return redirect("todo-task", id=obj.id)
    else:
        form = NewTaskForm(instance=obj)
   



    author = request.user
    tasksNotCleaned = Task.objects.filter(author=author)
    tasks = [{"title": x[2], "id": x[0]} for x in tasksNotCleaned.values_list()]
    context = {"tasks":tasks, "form":form}
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
            return redirect("todo-task", id=task.id)
        
    else:
        form = NewTaskForm()
    context=  {"form": form} 
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



