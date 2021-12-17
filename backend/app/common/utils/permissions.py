from typing import List, Type

from rest_framework.permissions import BasePermission


def method_permission(permissions: List[Type[BasePermission]]):
    """
    :param permissions: list of permissions
    :return: method api view

    Set custom permission for each method ApiView
    """
    def wrapper(func):
        def method(self, request, *args, **kwargs):
            self.permission_classes = permissions
            self.check_permissions(request)
            return func(self, request, *args, **kwargs)

        return method

    return wrapper
