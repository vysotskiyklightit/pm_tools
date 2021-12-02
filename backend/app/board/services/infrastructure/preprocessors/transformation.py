from typing import Type

from board.serializers.board import BoardCreateSerializer

from .base import SerializerDataPreprocessorBase


class BoardDataPreprocessor(SerializerDataPreprocessorBase):
    serializer_class: Type[
        BoardCreateSerializer
    ] = BoardCreateSerializer
