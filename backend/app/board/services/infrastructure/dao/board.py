from dataclasses import dataclass

from board.models import Board
from board.services.infrastructure.dao.base import BaseDAO
from django.db.models import QuerySet


@dataclass
class BoardEntity:
    pass


class BoardDAO(BaseDAO[Board, BoardEntity]):

    def fetch(self) -> QuerySet:
        queryset = self._model.objects.all()
        return queryset


board_dao = BoardDAO(Board)
