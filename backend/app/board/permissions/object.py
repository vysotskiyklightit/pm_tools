from typing import Union

from board.models import Board, Column, Ticket
from rest_framework.permissions import (SAFE_METHODS, BasePermission,
                                        IsAuthenticated)

from ..config.common import BoardPreference
from .group import IsPM
from .helpers import (ContributorBoardSelectorFieldMixin, IsAuthenticatedMixin,
                      OwnerBoardSelectorFieldMixin, SelectorBoardPath)


class IsOwnerBoard(
    IsAuthenticated,
    OwnerBoardSelectorFieldMixin
):
    message = 'You do not have access for this object'
    code = 403

    def has_permission(self, request, view):
        obj = SelectorBoardPath().get_model_object(view.kwargs)
        return obj and self._get_instance(obj) == request.user

    def has_object_permission(self, request, view,
                              obj: Union[Board, Column, Ticket]):
        return self._get_instance(obj) == request.user


class IsContributor(
    IsAuthenticated,
    ContributorBoardSelectorFieldMixin
):
    message = 'You do not have access for this object'
    code = 403

    def has_permission(self, request, view):
        obj = SelectorBoardPath().get_model_object(view.kwargs)
        return obj and request.user in self._get_instance(obj).all()

    def has_object_permission(self, request, view,
                              obj: Union[Board, Column, Ticket]):
        return request.user in self._get_instance(obj).all()


class IsPMBoard(IsPM, IsContributor):
    pass


class IsContributorOrOwnerBoard(BasePermission):

    def has_object_permission(self, request, view, obj: Board):
        is_contributor = IsContributor().has_object_permission(
            request, view, obj)
        is_owner = IsOwnerBoard().has_object_permission(
            request, view, obj)

        return is_contributor or is_owner

    def has_permission(self, request, view):
        is_contributor = IsContributor().has_permission(
            request, view)
        is_owner = IsOwnerBoard().has_permission(
            request, view)

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
