from django.db import models
from django.forms.widgets import CheckboxInput
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task_title = models.CharField(null= True, max_length=50)
    task_content = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.task_title
    

