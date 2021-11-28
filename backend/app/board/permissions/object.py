from typing import Union

from board.models import Board, Column, Ticket
from rest_framework.permissions import SAFE_METHODS, BasePermission

from ..config.common import BoardPreference
from .group import IsPM
from .helpers import (IsAuthenticatedMixin, SelectorBoardPath,
                      SelectorFieldMixin)


class IsOwnerBoard(BasePermission, IsAuthenticatedMixin, SelectorFieldMixin):
    INSTANCE_FIELD_NAME: str = 'owner'
    message = 'You do not have access for this object'
    code = 403

    def has_permission(self, request, view):
        return self._permission_request_owner(request, view)

    def has_object_permission(self, request, view,
                              obj: Union[Board, Column, Ticket]):
        return self._permission_object_owner(request, view, obj)

    def _permission_request_owner(self, request, view):
        self.request = request
        obj = SelectorBoardPath().get_model_object(view.kwargs)
        return bool(obj and self._is_authenticated
                    and self._get_instance(obj) == request.user)

    def _permission_object_owner(self, request, view,
                                 obj: Union[Board, Column, Ticket]):
        return self._get_instance(obj) == request.user


class IsContributorBoard(BasePermission,
                         IsAuthenticatedMixin,
                         SelectorFieldMixin):
    INSTANCE_FIELD_NAME: str = 'contributors'
    message = 'You do not have access for this object'
    code = 403

    def has_permission(self, request, view):
        return self._permission_request_contributor(request, view)

    def has_object_permission(self, request, view,
                              obj: Union[Board, Column, Ticket]):
        return self._permission_object_contributor(request, view, obj)

    def _permission_request_contributor(self, request, view):
        self.request = request
        obj = SelectorBoardPath().get_model_object(view.kwargs)
        return bool(obj and self._is_authenticated
                    and request.user in self._get_instance(obj).all())

    def _permission_object_contributor(self, request, view,
                                       obj: Union[Board, Column, Ticket]):
        return request.user in self._get_instance(obj).all()


class IsPMBoard(IsPM, IsContributorBoard):
    pass


class IsContributorOrOwnerBoard(IsOwnerBoard, IsContributorBoard):

    def has_object_permission(self, request, view, obj: Board):
        is_contributor = self._permission_object_contributor(
            request, view, obj)
        is_owner = self._permission_object_owner(
            request, view, obj)
        return is_contributor or is_owner

    def has_permission(self, request, view):
        is_contributor = self._permission_request_contributor(request, view)
        is_owner = self._permission_request_owner(request, view)
        return is_contributor or is_owner


class ByPreferenceRule(BasePermission, IsAuthenticatedMixin):

    def has_object_permission(self, request, view, obj: Board):
        self.request = request
        is_private_board = obj.preference == BoardPreference.private.value
        is_owner = self.request.user == obj.owner
        is_contributor = self.request.user in obj.contributors.all()
        is_auth = self._is_authenticated()
        is_safe_method = self.request.method in SAFE_METHODS
        return bool((not is_private_board and is_auth and is_safe_method)
                    or (is_owner or is_contributor))
