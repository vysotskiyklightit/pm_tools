from typing import Type, TypeVar, Union

from common.interfaces import IPresenter
from django.db.models import Model, QuerySet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer

SerializerType = TypeVar('SerializerType', bound=BaseSerializer)
InstanceType = TypeVar('InstanceType', bound=Model)


class SerializerPresenter(IPresenter):

    serializer_class: Type[SerializerType] = None
    success_status = status.HTTP_201_CREATED

    def __init__(self, instance: Union[InstanceType, QuerySet],
                 response_status: int = status.HTTP_200_OK,
                 is_list: bool = False):
        self._instance: Union[InstanceType, QuerySet] = instance
        self._status: int = response_status
        self._is_list: bool = is_list

    def _prepare_response(
            self,
            serializer: SerializerType
    ) -> Response:
        return Response(serializer.data, status=self._status)

    def _get_serializer(self) -> SerializerType:
        return self.serializer_class(self._instance, many=self._is_list)
