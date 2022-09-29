from datetime import datetime
from django.db import models
from boards.models import Board
from django_enumfield import enum
from django.utils.translation import gettext_lazy

# Create your models here.


class ColorsEnum(enum.Enum):
    BLUE = 0
    PURPLE = 1
    GREEN = 2
    RED = 3
    YELLOW = 4

    __labels__ = {
        BLUE: gettext_lazy('#49C4E5'),
        PURPLE: gettext_lazy('#8471F2'),
        GREEN: gettext_lazy('#67E2AE'),
        RED: gettext_lazy('#ef233c'),
        YELLOW: gettext_lazy('#ffd60a'),
    }


class Column(models.Model):
    name = models.CharField(max_length=100, default="New")
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now)
    color = enum.EnumField(ColorsEnum, default=ColorsEnum.BLUE)
