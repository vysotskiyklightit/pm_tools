from board.config.common import SystemUsers
from django.contrib.auth.models import Group
from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

from .helpers import IsAuthenticatedMixin


class IsPM(permissions.BasePermission, IsAuthenticatedMixin):

    def has_permission(self, request, view):
        self.request = request
        return bool(self._is_pm()
                    or (self._is_safe_method()
                        and self._is_authenticated()))

    def _is_pm(self):
        manager_group = Group.objects.get(name=SystemUsers.managers.value)
        return manager_group in self.request.user.groups.all()

    def _is_safe_method(self):
        return self.request.method in SAFE_METHODS
