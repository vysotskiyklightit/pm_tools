from board.models import Board, Column
from board.permissions.board import (ByPreferenceRule, IsOwnerBoard, IsPM,
                                     IsPMBoard)
from board.serializers.board import (BoardCreateSerializer,
                                     BoardListSerializer,
                                     BoardRetrieveSerializer,
                                     BoardUpdateSerializer,
                                     ColumnCreateUpdateSerializer,
                                     ColumnListSerializer)
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   RetrieveModelMixin, UpdateModelMixin)
from rest_framework.permissions import IsAuthenticated


class BoardCreateListView(
    GenericAPIView,
    CreateModelMixin,
    ListModelMixin
):
    queryset = Board.objects.all()
    serializer_class = BoardCreateSerializer

    def get(self, request):
        self.permission_classes = [IsAuthenticated]
        self.serializer_class = BoardListSerializer
        return self.list(request)

    def post(self, request):
        self.permission_classes = [IsAuthenticated, IsPM]
        return self.create(request)


class BoardUpdateRetrieveView(
    GenericAPIView,
    UpdateModelMixin,
    RetrieveModelMixin
):
    queryset = Board.objects.all()
    lookup_field = 'id'

    def put(self, request):
        self.permission_classes = [IsAuthenticated, IsOwnerBoard, IsPMBoard]
        self.serializer_class = BoardUpdateSerializer
        return self.update(request)

    def get(self, request):
        self.permission_classes = [IsAuthenticated, ByPreferenceRule]
        self.serializer_class = BoardRetrieveSerializer
        return self.retrieve(request)


class ColumnListCreateView(
    GenericAPIView,
    CreateModelMixin,
    ListModelMixin
):
    queryset = Column.objects.all()
    serializer_class = ColumnCreateUpdateSerializer

    def get(self, request, board_id):
        self.permission_classes = [IsAuthenticated]
        self.serializer_class = ColumnListSerializer

        self.board_id = board_id
        return self.list(request)

    def post(self, request, board_id):
        self.permission_classes = [IsAuthenticated, IsOwnerBoard, IsPMBoard]

        request.data['board'] = board_id
        return self.create(request)

    def get_queryset(self):
        return self.queryset.filter(board_id=self.board_id)


class ColumnUpdateRetrieveView(
    GenericAPIView,
    UpdateModelMixin,
    RetrieveModelMixin
):
    queryset = Column.objects.all()
    lookup_field = 'id'
