from board.config.utils import IService
from board.serializers.board import BoardCreateSerializer


class BoardCreateService(IService):

    def __init__(
            self,
            serializer: BoardCreateSerializer,

    ):
        pass

    def execute(self):
        pass

    def _validate(self):
        pass

    def _save(self):
        pass
