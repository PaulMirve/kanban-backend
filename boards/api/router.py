from rest_framework.routers import DefaultRouter
from boards.api.views import BoardsViewSet

board_router = DefaultRouter()
board_router.register(r'board', BoardsViewSet)
