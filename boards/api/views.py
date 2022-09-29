from rest_framework.viewsets import ModelViewSet
from boards.models import Board
from boards.api.serializer import BoardSerializer
from rest_framework.permissions import IsAuthenticated


class BoardsViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Board.objects.filter(user=user).order_by("date_created")
