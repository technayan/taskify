from django.shortcuts import render, redirect
from .forms import addTaskForm
from .models import Task

# Create your views here.
def addTask (req):
    if req.method == "POST":
        form = addTaskForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = addTaskForm()
    return render (req, 'task/add_task.html', {'form': form})


def editTask (req, id):
    task = Task.objects.get(pk = id)
    form = addTaskForm(instance=task)
    if req.method == "POST":
        form = addTaskForm(req.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render (req, 'task/edit_task.html', {'form': form})


def deleteTask (req, id):
    task = Task.objects.get(pk = id)
    task.delete()
    return redirect('home')