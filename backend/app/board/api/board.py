from board.api.bases import PathDependsRelationBoardAPIView
from board.config.utils import method_permission
from board.models import Board, Column
from board.permissions import (ByPreferenceRule, IsContributorOrOwnerBoard,
                               IsOwnerBoard, IsPM, IsPMBoard)
from board.serializers.board import (BoardCreateListSerializer,
                                     BoardRetrieveUpdateSerializer,
                                     ColumnCreateSerializer,
                                     ColumnListRetrieveSerializer,
                                     ColumnUpdateSerializer)
from board.services.application.usecases.board import BoardCreateCase
from board.services.infrastructure.presenters.board import BoardPresenter
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.request import Request


class BoardCreateListView(
    GenericAPIView,
    CreateModelMixin,
    ListModelMixin
):
    queryset = Board.objects.all()
    serializer_class = BoardCreateListSerializer

    @method_permission([ByPreferenceRule])
    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @method_permission([IsPM])
    def post(self, request: Request, *args, **kwargs):
        self.request.data['owner'] = request.user.id
        serializer = self.get_serializer(data=self.request.data)

        board: Board = BoardCreateCase(serializer).execute()
        return BoardPresenter(board).present()


class BoardUpdateRetrieveView(
    GenericAPIView,
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin
):
    queryset = Board.objects.all()
    serializer_class = BoardRetrieveUpdateSerializer
    lookup_field = 'id'

    @method_permission([IsContributorOrOwnerBoard])
    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @method_permission([IsOwnerBoard, IsPMBoard])
    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @method_permission([IsOwnerBoard, IsPMBoard])
    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ColumnListCreateView(
    PathDependsRelationBoardAPIView,
    CreateModelMixin,
    ListModelMixin
):
    queryset = Column.objects.all()
    serializer_class = ColumnCreateSerializer

    @method_permission([IsContributorOrOwnerBoard])
    def get(self, request, *args, **kwargs):
        self.serializer_class = ColumnListRetrieveSerializer
        return self.list(request, *args, **kwargs)

    @method_permission([IsOwnerBoard, IsPMBoard])
    def post(self, request, *args, **kwargs):
        return self.create(self.request)


class ColumnUpdateRetrieveDeleteView(
    PathDependsRelationBoardAPIView,
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin
):
    queryset = Column.objects.all()
    lookup_field = 'id'
    serializer_class = ColumnUpdateSerializer

    @method_permission([IsContributorOrOwnerBoard])
    def get(self, request, *args, **kwargs):
        self.serializer_class = ColumnListRetrieveSerializer
        return self.retrieve(request, *args, **kwargs)

    @method_permission([IsOwnerBoard, IsPMBoard])
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @method_permission([IsOwnerBoard])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
