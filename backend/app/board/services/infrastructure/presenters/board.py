from typing import Type

from board.serializers.board import (BoardListSerializer,
                                     BoardRetrieveUpdateSerializer)
from board.services.infrastructure.presenters.base import SerializerPresenter
from rest_framework import status
from rest_framework.response import Response


class BoardPresenter(SerializerPresenter):
    serializer_class: Type[
        BoardRetrieveUpdateSerializer] = BoardRetrieveUpdateSerializer

    def present(self) -> Response:
        self._status = status.HTTP_201_CREATED
        serializer = self._get_serializer()
        return self._prepare_response(serializer)


class BoardListPresenter(SerializerPresenter):
    serializer_class: Type[
        BoardListSerializer] = BoardListSerializer

    def present(self) -> Response:
        self._is_list = True
        serializer = self._get_serializer()
        return self._prepare_response(serializer)
