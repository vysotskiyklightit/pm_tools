from rest_framework import permissions


class IsPM(permissions.BasePermission):
    pass


class IsOwnerBoard(permissions.BasePermission):
    pass


class IsPMBoard(permissions.BasePermission):
    pass


class IsContributorOrOwnerBoard(permissions.BasePermission):
    pass


class ByPreferenceRule(IsContributorOrOwnerBoard):
    pass
