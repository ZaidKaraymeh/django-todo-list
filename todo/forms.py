from django import forms
from django.forms.widgets import CheckboxInput
from .models import Project, Task


class NewTaskForm(forms.ModelForm):
    # task_done = forms.BooleanField(required=False, widget= CheckboxInput)


    class Meta:
        model = Task
        fields = ["task_title", "task_content"]
    



class NewProjectForm(forms.ModelForm):
    # task_done = forms.BooleanField(required=False, widget= CheckboxInput)


    class Meta:
        model = Project
        fields = ["project_title"]
    class Media:
        js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.
        css = {
            'all': ('ckeditor/contents.css',)
        }
