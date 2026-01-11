# Model for the todo list part of the application

from django.db import models

''' Define model for the todo list part of the application
Including fields for:
- Title (max 100 characters)
- Tick boxes (boolean for completion status)
- Entries of the todo list (max 300 characters)
- Estimated due date (date field - format 08 Jan 2026)
- Author name (max 50 characters)
Include a __str__ representation method that returns the title of the todo list.
'''


class TodoList(models.Model):
    title = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    entry = models.TextField(max_length=300)
    estimated_due_date = models.DateField()
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title
