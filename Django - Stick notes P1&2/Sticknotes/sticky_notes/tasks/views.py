# module to define views for tasks in the sticky notes application


from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from todo_list.models import TodoList


# Function to render the home view showing both tasks and todos
def home_view(request):
    tasks = Task.objects.all().order_by('-entry_date')
    todos = TodoList.objects.all().order_by('estimated_due_date')
    return render(request, 'tasks/home.html', {'tasks': tasks, 'todos': todos})


# Function to list all tasks
def task_list(request):
    tasks = Task.objects.all().order_by('-entry_date')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


# Function to view details of a specific task
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})


# Function to create a new task
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})


# Function to edit an existing task
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})


# Function to delete a task
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')


# Function to mark a task as completed
def task_mark_completed(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = True
    task.save()
    return redirect('task_detail', pk=task.pk)
