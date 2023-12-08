from django import forms
from .models import Task

class addTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_title', 'task_description', 'category', 'is_complete']
        widgets = {
            'task_description': forms.Textarea(attrs={'rows':3})
        }