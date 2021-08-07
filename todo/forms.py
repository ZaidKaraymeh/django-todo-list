from django import forms
from django.forms.widgets import CheckboxInput
from .models import Task


class NewTaskForm(forms.ModelForm):
    # task_done = forms.BooleanField(required=False, widget= CheckboxInput)


    class Meta:
        model = Task
        fields = ["task_title", "task_content"]
