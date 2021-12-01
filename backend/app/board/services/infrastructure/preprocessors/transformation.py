from typing import Type

from board.serializers.board import BoardCreateListSerializer

from .base import SerializerDataPreprocessorBase


class BoardDataPreprocessor(SerializerDataPreprocessorBase):
    serializer_class: Type[
        BoardCreateListSerializer
    ] = BoardCreateListSerializer
