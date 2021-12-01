from board.config.common import BoardPreference
from board.config.utils import IService
from board.services.infrastructure.dao.board import board_dao
from django.contrib.auth.models import User
from django.db.models import Q, QuerySet


class BoardListService(IService):
    def __init__(self, user: User):
        self._user: User = user

    def execute(self) -> QuerySet:
        self._boards = board_dao.fetch()
        return self._filter_by_preference()

    def _filter_by_preference(self) -> QuerySet:
        public_boards = self._boards.filter(
            preference=BoardPreference.public.value)
        private_users_boards = self._boards.filter(
            Q(owner__pk=self._user.id) | Q(contributors__pk=self._user.id))
        return public_boards.union(private_users_boards)
