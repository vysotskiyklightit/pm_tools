from board.models import Board
from board.services.domain.lists import BoardListService
from board.services.domain.utils import ColumnDefaultEntities
from board.services.infrastructure.preprocessors.transformation import \
    BoardDataPreprocessor
from django.contrib.auth.models import User
from django.db.models import QuerySet

from .base import BaseCreateCase, BaseListCase


class BoardCreateCase(BaseCreateCase):

    def create(self) -> Board:
        self._serializer = self._preprocess_data()
        self._create()

        board = self._get_board()
        ColumnDefaultEntities(board_id=board.id).execute()
        return board

    def _preprocess_data(self):
        return BoardDataPreprocessor(self._request).process()

    def _create(self):
        self._serializer.save()

    def _get_board(self) -> Board:
        return self._serializer.instance


class BoardListCase(BaseListCase):
    queryset: QuerySet = None

    def list(self) -> QuerySet:
        user: User = self._request.user
        list_service = BoardListService(user)
        return list_service.execute()
