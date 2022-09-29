from datetime import datetime
from django.db import models
from users.models import User

# Create your models here.


class Board(models.Model):
    name = models.CharField(max_length=150, default="New")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now);
