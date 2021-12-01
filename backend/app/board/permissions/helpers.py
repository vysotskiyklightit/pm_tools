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
