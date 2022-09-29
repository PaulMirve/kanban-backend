from rest_framework.viewsets import ModelViewSet
from tasks.api.serializer import TaskSerializer, SubtaskSerializer
from tasks.models import Task, Subtask


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class SubTaskVieSet(ModelViewSet):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer
