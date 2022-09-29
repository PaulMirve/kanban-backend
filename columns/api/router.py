from rest_framework.routers import DefaultRouter
from columns.api.views import ColumnsViewSet

column_router = DefaultRouter()
column_router.register(r'column', ColumnsViewSet)
