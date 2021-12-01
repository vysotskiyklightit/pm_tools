from board.config.common import SystemUsers
from django.contrib.auth.models import Group, User
from rest_framework.permissions import SAFE_METHODS, BasePermission

from .helpers import IsAuthenticatedMixin


class IsPM(BasePermission, IsAuthenticatedMixin):

    def has_permission(self, request, view):
        self.request = request
        return bool(self._is_pm()
                    or (self._is_safe_method()
                        and self._is_authenticated()))

    def _is_pm(self):
        manager_group = Group.objects.get(name=SystemUsers.managers.value)
        user = User.objects.get(id=self.request.user.id)
        return manager_group.id in [g.id for g in user.groups.all()]

    def _is_safe_method(self):
        return self.request.method in SAFE_METHODS
