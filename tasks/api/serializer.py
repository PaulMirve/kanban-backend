from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from tasks.models import Task, Subtask
from rest_framework import serializers


class SubtaskSerializer(ModelSerializer):
    class Meta:
        model = Subtask
        fields = "__all__"


class TaskSerializer(ModelSerializer):
    subtasks = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = "__all__"

    def get_subtasks(self, obj):
        subtasks = Subtask.objects.filter(task=obj)
        return SubtaskSerializer(subtasks, many=True).data
