# Model for the user input forms for the todo list part of the application

from django import forms
from .models import TodoList

''' Define forms for the todo list part of the application
Including fields for:
- Title
- Entry
- Author
- Estimated due date
- Tick boxes (boolean for completion status)
'''


class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title', 'entry', 'author', 'estimated_due_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'entry': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'estimated_due_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'is_completed': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
            ),
        }
