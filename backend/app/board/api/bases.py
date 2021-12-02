from typing import List

from board.filters.path import PathParamsFilter
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request


class PathDependsRelationBaseAPIView(GenericAPIView):
    """
    To pull up the entire chain of dependencies in an object.
    With this method, I can only specify permissions for the
    head of the dependency chain.
    """

    defaults_path_filters: list = None

    def initialize_request(self, request, *args, **kwargs):
        request = super().initialize_request(request, *args, **kwargs)
        self._add_path_filter_backend()
        return request

    def _add_path_filter_backend(self):
        self.filter_backends += self.defaults_path_filters


class PathDependsRelationBoardAPIView(PathDependsRelationBaseAPIView):
    defaults_path_filters: list = [PathParamsFilter]
