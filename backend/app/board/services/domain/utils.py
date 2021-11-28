from typing import Iterable, List

from board.config.utils import IService
from board.services.infrastructure.dao.column import ColumnEntity, column_dao


class ColumnDefaultEntities(IService):
    _DEFAULTS_COLUMNS: List[str] = [
        'To do',
        'n progress',
        'Done',
    ]

    def __init__(self, board_id):
        self._broad_id = board_id

    def execute(self) -> Iterable[ColumnEntity]:
        for name in self._DEFAULTS_COLUMNS:
            yield column_dao.create(name=name, board_id=self._broad_id)
