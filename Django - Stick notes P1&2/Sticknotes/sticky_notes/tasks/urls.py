# module to define URLs for tasks in the sticky notes application

from django.urls import path
from .views import (
    home_view,
    task_list,
    task_detail,
    task_create,
    task_edit,
    task_delete,
    task_mark_completed,
)

urlpatterns = [
    # Home page showing both tasks and todos
    path('', home_view, name='home'),

    # List all tasks
    path('list/', task_list, name='task_list'),

    # View details of a specific task
    path('task/<int:pk>/', task_detail, name='task_detail'),

    # Create a new task
    path('task/new/', task_create, name='task_create'),

    # Edit an existing task
    path('task/<int:pk>/edit/', task_edit, name='task_edit'),

    # Mark a task as completed
    path('task/<int:pk>/complete/', task_mark_completed,
         name='task_mark_completed'),

    # Delete a task
    path('task/<int:pk>/delete/', task_delete, name='task_delete'),
]
