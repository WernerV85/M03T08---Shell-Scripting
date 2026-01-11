# Model to define URLs for the todo list  in the sticky notes application

from django.urls import path
from .views import (
    todo_list,
    todo_detail,
    todo_create,
    todo_edit,
    todo_mark_completed,
    todo_delete,
)

urlpatterns = [
    # List all todo list entries
    path('', todo_list, name='todo_list'),

    # View details of a specific todo list entry
    path('todo/<int:pk>/', todo_detail, name='todo_detail'),

    # Create a new todo list entry
    path('todo/new/', todo_create, name='todo_create'),

    # Edit an existing todo list entry
    path('todo/<int:pk>/edit/', todo_edit, name='todo_edit'),

    # Mark a todo list entry as completed
    path(
        'todo/<int:pk>/complete/',
        todo_mark_completed,
        name='todo_mark_completed'
    ),

    # Delete a todo list entry
    path('todo/<int:pk>/delete/', todo_delete, name='todo_delete'),
]
