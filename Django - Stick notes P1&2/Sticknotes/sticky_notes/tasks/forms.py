# Module for the user input forms for the task part of the application

from django import forms
from .models import Task

''' Define forms for the task part of the application
Including fields for:
- Title
- Description
- Author
- Due date (optional)
- Priority
- Category
'''


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title', 'description', 'author', 'due_date', 'priority',
            'category'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
