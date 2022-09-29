from rest_framework.viewsets import ModelViewSet
from columns.api.serializers import ColumnSerializer
from columns.models import Column
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated


class ColumnsViewSet(ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET'], url_path=r'board/(?P<board_id>\d+)', name="Get board's columns")
    def board(self, request, board_id):
        columns = Column.objects.filter(board=board_id).order_by("date_created")
        serialized_data = ColumnSerializer(columns, many=True).data
        return Response(serialized_data)
