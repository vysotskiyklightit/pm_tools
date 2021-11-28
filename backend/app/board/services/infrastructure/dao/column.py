from dataclasses import dataclass

from board.models import Column
from board.services.infrastructure.dao.base import BaseDAO


@dataclass
class ColumnEntity:
    id: int
    name: str
    board_id: int


class ColumnDAO(BaseDAO[Column, ColumnEntity]):

    def _to_entity(self, instance: Column) -> ColumnEntity:
        return ColumnEntity(
            id=instance.pk,
            name=instance.name,
            board_id=instance.board.id
        )

    def create(self, *, name: str, board_id: int) -> ColumnEntity:
        return self._to_entity(
            self._model(board_id=board_id, name=name).save()
        )


column_dao = ColumnDAO(Column)
