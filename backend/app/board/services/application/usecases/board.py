from board.config.utils import IService
from board.models import Board
from board.serializers.board import BoardCreateListSerializer
from board.services.domain.default_entities import ColumnDefaultEntities


class BoardCreateCase(IService):

    def __init__(self, serializer: BoardCreateListSerializer):
        self._serializer = serializer

    def execute(self) -> Board:
        self._validate()
        self._serializer.save()
        board = self._get_board()
        ColumnDefaultEntities(board_id=board.id).execute()
        return board

    def _validate(self):
        self._serializer.is_valid(raise_exception=True)

    def _get_board(self):
        return self._serializer.instance
