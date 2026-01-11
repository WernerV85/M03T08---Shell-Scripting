# Task model

from django.db import models

''' Define model for the task part of the application
Including fields for:
- Title (max 100 characters)
- Description (max 500 characters)
- Author (max 50 characters)
- Entry date (auto set on creation - format 08 Jan 2026)
- Completion status (boolean)
- Due date (optional)
- Priority level (Low/Medium/High/Urgent)
- Category (Work/Personal/Shopping/Other)

Include a __str__ representation method that returns the title of the task.'''


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]

    CATEGORY_CHOICES = [
        ('work', 'Work'),
        ('personal', 'Personal'),
        ('shopping', 'Shopping'),
        ('health', 'Health'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    author = models.CharField(max_length=50)
    entry_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default='medium'
    )
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default='other'
    )

    def __str__(self):
        return self.title
