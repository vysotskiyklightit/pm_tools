from typing import Union

from board.models import Board, Column, Ticket
from rest_framework.permissions import BasePermission

from .group import IsPM
from .helpers import (ContributorBoardPermission, IsAuthenticatedMixin,
                      OwnerBoardPermission)


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
        return bool(
            IsPMBoard().has_object_permission(request, view, obj)
            or IsOwnerBoard().has_object_permission(request, view, obj))


class IsContributorOrOwnerBoard(BasePermission,
                                IsAuthenticatedMixin):

    def has_permission(self, request, view):
        self.request = request
        return self._is_authenticated()

    def has_object_permission(self, request, view, obj: Board):
        return bool(obj.owner == request.user
                    or request.user in obj.contributors.all())


class IsOwnerBoardFromPath(BasePermission,
                           IsAuthenticatedMixin):
    message = 'You do not have access for this object'
    code = 403

    def has_permission(self, request, view):
        self.request = request
        object_permission = OwnerBoardPermission(request, view)
        return bool(object_permission.permission_request()
                    and self._is_authenticated)

    def has_object_permission(self, request, view,
                              obj: Union[Board, Column, Ticket]):
        object_permission = OwnerBoardPermission(request, view)
        return object_permission.permission_object(obj)


class IsContributorBoardFromPath(BasePermission,
                                 IsAuthenticatedMixin):
    message = 'You do not have access for this object'
    code = 403

    def has_permission(self, request, view):
        self.request = request
        object_permission = ContributorBoardPermission(request, view)
        return bool(self._is_authenticated
                    and object_permission.permission_request())

    def has_object_permission(self, request, view,
                              obj: Union[Board, Column, Ticket]):
        object_permission = ContributorBoardPermission(request, view)
        return object_permission.permission_object(obj)


class IsPMBoardFromPath(IsPM, IsContributorBoardFromPath):
    pass


class IsContributorOrOwnerBoardFromPath(BasePermission,
                                        IsAuthenticatedMixin):

    def has_permission(self, request, view):
        self.request = request

        is_contributor = ContributorBoardPermission(
            request, view).permission_request()
        is_owner = OwnerBoardPermission(request, view).permission_request()

        return (is_contributor or is_owner) and self._is_authenticated()

    def has_object_permission(self, request, view, obj: Board):
        is_contributor = ContributorBoardPermission(
            request, view).permission_object(obj)
        is_owner = OwnerBoardPermission(request, view).permission_object(obj)

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
