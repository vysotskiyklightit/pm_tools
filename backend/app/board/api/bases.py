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

    lookup_relation_fields: List[str] = None
    defaults_path_filters: list = None

    def initialize_request(self, request, *args, **kwargs):
        request = super().initialize_request(request, *args, **kwargs)
        self._add_path_filter_backend()
        return self._prepare_request(request)

    def _prepare_request(self, request) -> Request:
        return self._add_params_to_request_data(request)

    def _add_params_to_request_data(self, request) -> Request:
        """
        Select path params and these to request data
        """
        for field_name in self.lookup_relation_fields:
            if field_name not in self.kwargs:
                continue
            request.data[field_name] = self.kwargs[field_name]
        return request

    def _add_path_filter_backend(self):
        self.filter_backends += self.defaults_path_filters


class PathDependsRelationBoardAPIView(PathDependsRelationBaseAPIView):
    lookup_relation_fields: List[str] = ['board', 'column', 'ticket']
    defaults_path_filters: list = [PathParamsFilter]
