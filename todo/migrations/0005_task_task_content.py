# Generated by Django 3.2.6 on 2021-08-07 13:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_remove_task_task_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]