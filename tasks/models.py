from datetime import datetime
from django.db import models
from columns.models import Column

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now);


class Subtask(models.Model):
    description = models.CharField(max_length=400)
    completed = models.BooleanField(default=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
