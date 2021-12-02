from typing import Any, Dict

from board.models import Board, Column, Ticket, TicketComment
from django.db.models import Model


class IsAuthenticatedMixin(object):

    def _is_authenticated(self):
        return bool(self.request.user and self.request.user.is_authenticated)


class SelectorFieldMixin(object):
    INSTANCE_FIELD_NAME: str = None
    _related_field_map: Dict[Model, str] = {
        TicketComment: 'ticket',
        Ticket: 'column',
        Column: 'board'
    }

    def _get_instance(self, obj) -> Any:
        instance = self._get_field_from_related(obj)
        return getattr(instance, self.INSTANCE_FIELD_NAME)

    def _get_field_from_related(self, obj) -> Model:
        for instance, field_name in self._related_field_map.items():
            if isinstance(obj, instance):
                obj = getattr(obj, field_name)
        return obj


class SelectorPathPKBase(object):
    lookup_field: str = None
    model: Model = None

    def get_model_object(self, params: dict):
        if self.lookup_field not in params:
            return None
        query = self.model.objects.filter(**{'id': params[self.lookup_field]})
        if not query.exists():
            return None
        return query.first()


class SelectorBoardPath(SelectorPathPKBase):
    lookup_field: str = 'board'
    model: Model = Board


class ObjectPathPermission(object):
    INSTANCE_FIELD_NAME: str = None

    def __init__(self, request, view):
        self._request = request
        self._view = view

    def permission_object(self, obj):
        raise NotImplementedError

    def permission_request(self):
        raise NotImplementedError


class OwnerBoardPermission(ObjectPathPermission, SelectorFieldMixin):
    INSTANCE_FIELD_NAME: str = 'owner'

    def permission_object(self, obj):
        return self._get_instance(obj) == self._request.user

    def permission_request(self):
        obj = SelectorBoardPath().get_model_object(self._view.kwargs)
        return bool(obj and self._get_instance(obj) == self._request.user)


class ContributorBoardPermission(ObjectPathPermission, SelectorFieldMixin):
    INSTANCE_FIELD_NAME: str = 'contributors'

    def permission_object(self, obj):
        return self._request.user in self._get_instance(obj).all()

    def permission_request(self):
        obj = SelectorBoardPath().get_model_object(self._view.kwargs)
        return bool(
            obj and self._request.user in self._get_instance(obj).all())
