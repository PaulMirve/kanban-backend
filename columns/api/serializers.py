from rest_framework.serializers import ModelSerializer
from columns.models import ColorsEnum, Column
from tasks.models import Task
from rest_framework import serializers
from tasks.api.serializer import TaskSerializer
from django_enumfield.enum import EnumField


class ColumnSerializer(ModelSerializer):
    tasks = serializers.SerializerMethodField()

    class Meta:
        model = Column
        fields = "__all__"

    def get_tasks(self, obj):
        tasks_list = Task.objects.filter(column=obj.id)
        return TaskSerializer(tasks_list, many=True).data;
