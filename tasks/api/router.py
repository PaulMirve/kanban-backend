from rest_framework.routers import DefaultRouter
from tasks.api.views import TaskViewSet, SubTaskVieSet

tasks_router = DefaultRouter()
tasks_router.register(r'tasks', TaskViewSet)
tasks_router.register(r'subtasks', SubTaskVieSet)
