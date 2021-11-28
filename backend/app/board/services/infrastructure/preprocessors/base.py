from typing import Type, TypeVar

from board.config.utils import IPreprocessors
from rest_framework.request import Request
from rest_framework.serializers import BaseSerializer

SerializerType = TypeVar('SerializerType', bound=BaseSerializer)


class SerializerDataPreprocessorBase(IPreprocessors):
    serializer_class: Type[SerializerType]

    def __init__(self, request: Request):
        self._request: Request = request

    def process(self) -> SerializerType:
        serializer = self.serializer_class()
        serializer.is_valid(raise_exception=True)
        return serializer

    def _get_serializer(self) -> SerializerType:
        return self.serializer_class(data=self._request.data)
