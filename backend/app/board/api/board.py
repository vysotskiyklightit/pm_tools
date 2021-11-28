from board.api.bases import PathDependsRelationBoardAPIView
from board.config.utils import method_permission
from board.models import Board, Column
from board.permissions import (IsContributorOrOwnerBoard, IsOwnerBoard, IsPM,
                               IsPMBoard)
from board.serializers.board import (BoardCreateListSerializer,
                                     BoardRetrieveUpdateSerializer,
                                     ColumnCreateSerializer,
                                     ColumnListRetrieveSerializer,
                                     ColumnUpdateSerializer)
from board.services.application.usecases.board import (BoardCreateCase,
                                                       BoardListCase)
from board.services.infrastructure.presenters.board import (BoardListPresenter,
                                                            BoardPresenter)
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView


class BoardCreateListView(APIView):
    """
    View for create or present list of board
    """

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: BoardCreateListSerializer()})
    @method_permission([IsAuthenticated])
    def get(self, request: Request, *args, **kwargs):
        boards = BoardListCase(request).list()
        return BoardListPresenter(boards).present()

    @swagger_auto_schema(
        request_body=BoardCreateListSerializer(),
        responses={status.HTTP_200_OK: BoardRetrieveUpdateSerializer()})
    @method_permission([IsPM])
    def post(self, request: Request, *args, **kwargs):
        board: Board = BoardCreateCase(request).create()
        return BoardPresenter(board).present()


class BoardUpdateRetrieveView(
    GenericAPIView,
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin
):
    """
    View for update delete, or present board
    """
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
    """
    View for create or present list of columns
    """
    queryset = Column.objects.all()
    serializer_class = ColumnCreateSerializer

    @swagger_auto_schema(tags=['column'])
    @method_permission([IsContributorOrOwnerBoard])
    def get(self, request, *args, **kwargs):
        self.serializer_class = ColumnListRetrieveSerializer
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(tags=['column'])
    @method_permission([IsOwnerBoard, IsPMBoard])
    def post(self, request, *args, **kwargs):
        return self.create(self.request)


class ColumnUpdateRetrieveDeleteView(
    PathDependsRelationBoardAPIView,
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin
):
    """
    View for update delete, or present column
    """
    queryset = Column.objects.all()
    serializer_class = ColumnUpdateSerializer
    lookup_field = 'id'

    @swagger_auto_schema(tags=['column'])
    @method_permission([IsContributorOrOwnerBoard])
    def get(self, request, *args, **kwargs):
        self.serializer_class = ColumnListRetrieveSerializer
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=['column'])
    @method_permission([IsOwnerBoard, IsPMBoard])
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['column'])
    @method_permission([IsOwnerBoard])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
