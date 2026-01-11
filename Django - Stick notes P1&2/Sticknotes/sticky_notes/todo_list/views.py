# Module to define views for the todo list application.

from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoList
from .forms import TodoListForm

''' Define views for the todo list part of the application
Including:
- View to list all todo list entries
- View to see details of a specific todo list entry
- View to create a new todo list entry
- View to edit an existing todo list entry - update description
- View to mark a todo list entry as completed
- View to delete a todo list entry
'''


# Function to list all todo list entries
def todo_list(request):
    todos = TodoList.objects.all().order_by('estimated_due_date')
    return render(request, 'todo_list/todo_list.html', {'todos': todos})


# Function to view details of a specific todo list entry
def todo_detail(request, pk):
    todo = get_object_or_404(TodoList, pk=pk)
    return render(request, 'todo_list/todo_detail.html', {'todo': todo})


# Function to create a new todo list entry
def todo_create(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoListForm()
    return render(request, 'todo_list/todo_form.html', {'form': form})


# Function to edit an existing todo list entry
def todo_edit(request, pk):
    todo = get_object_or_404(TodoList, pk=pk)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoListForm(instance=todo)
    return render(request, 'todo_list/todo_form.html', {'form': form})


# Function to mark a todo list entry as completed
def todo_mark_completed(request, pk):
    todo = get_object_or_404(TodoList, pk=pk)
    todo.is_completed = True
    todo.save()
    return redirect('todo_detail', pk=todo.pk)


# Function to delete a todo list entry
def todo_delete(request, pk):
    todo = get_object_or_404(TodoList, pk=pk)
    todo.delete()
    return redirect('todo_list')
