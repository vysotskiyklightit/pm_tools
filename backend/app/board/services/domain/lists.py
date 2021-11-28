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
        preference_board = self._filter_by_preference()
        return preference_board

    def _filter_by_preference(self) -> QuerySet:
        # TODO !!!!!!!!!!!!!!!!!!!!!!!!
        public_boards = self._boards.filter(
            preference=BoardPreference.public.value)
        private_users_boards = self._boards.filter(
            Q(owner__pk=self._user.id) | Q(contributors__pk=self._user.id))
        print(private_users_boards, self._user.id)
        return public_boards.union(private_users_boards)
