from typing import Type

from board.config.utils import IPresenter
from board.models import Board
from board.serializers.board import BoardRetrieveUpdateSerializer
from rest_framework import status
from rest_framework.response import Response


class BoardPresenter(IPresenter):
    serializer_class: Type[
        BoardRetrieveUpdateSerializer] = BoardRetrieveUpdateSerializer
    created_status = status.HTTP_201_CREATED

    def __init__(self, board: Board):
        self._board = board

    def present(self):
        serializer = self._get_serializer()
        return self._prepare_response(serializer)

    def _prepare_response(
            self,
            serializer: BoardRetrieveUpdateSerializer
    ) -> Response:
        return Response(serializer.data, status=self.created_status)

    def _get_serializer(self) -> BoardRetrieveUpdateSerializer:
        return self.serializer_class(self._board)
