from typing import Union

from board.models import Board, Column, Ticket
from rest_framework.permissions import BasePermission

from .group import IsPM
from .helpers import (IsAuthenticatedMixin, SelectorBoardPath,
                      SelectorFieldMixin)


class IsOwnerBoard(BasePermission,
                   IsAuthenticatedMixin):
    def has_permission(self, request, view):
        self.request = request
        return self._is_authenticated()

    def has_object_permission(self, request, view, obj: Board):
        return obj.owner == request.user


class IsContributorBoard(IsOwnerBoard):

    def has_object_permission(self, request, view, obj: Board):
        return request.user in obj.contributors.all()


class IsPMBoard(IsPM, IsContributorBoard):
    pass


class IsOwnerOrPMBoard(BasePermission):
    def has_permission(self, request, view):
        return bool(IsPMBoard().has_permission(request, view)
                    or IsOwnerBoard().has_permission(request, view))

    def has_object_permission(self, request, view, obj: Board):
        return bool(IsPMBoard().has_object_permission(request, view, obj)
                    or IsOwnerBoard().has_object_permission(request, view, obj)
                    )


class IsContributorOrOwnerBoard(BasePermission,
                                IsAuthenticatedMixin):

    def has_permission(self, request, view):
        self.request = request
        return self._is_authenticated()

    def has_object_permission(self, request, view, obj: Board):
        return bool(obj.owner == request.user
                    or request.user in obj.contributors.all())


class IsOwnerBoardFromPath(BasePermission,
                           IsAuthenticatedMixin,
                           SelectorFieldMixin):
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


class IsContributorBoardFromPath(BasePermission,
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


class IsPMBoardFromPath(IsPM, IsContributorBoardFromPath):
    pass


class IsContributorOrOwnerBoardFromPath(IsOwnerBoardFromPath,
                                        IsContributorBoardFromPath):

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


class IsOwnerOrPMBoardFromPath(BasePermission):

    def has_permission(self, request, view):
        return bool(IsPMBoardFromPath().has_permission(request, view)
                    or IsOwnerBoardFromPath().has_permission(request, view))

    def has_object_permission(self, request, view, obj: Board):
        return bool(
            IsPMBoardFromPath().has_object_permission(request, view, obj)
            or IsOwnerBoardFromPath().has_object_permission(request, view, obj)
        )
