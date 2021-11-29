import pytest
from board.config.common import BoardPreference
from board.models import Board
from django.contrib.auth.models import User


class TestBoardApi(object):
    scenarios = [
        ('ERROR', {'username': 'den',
                   }),
        ('ERROR', {'username': 'den',
                   }),
        ('ERROR', {'username': 'den',
                   }),
        ('ERROR', {'username': 'den',
                   }),
        ('ERROR', {'username': 'den',
                   }),
    ]

    @pytest.mark.django_db(transaction=True)
    def test_get_list(self, api_client,
                      user,
                      create_pm,
                      create_contribs,
                      auth_header,
                      create_board,
                      status_code
                      ):
        api_client.credentials(**auth_header)
        r = api_client.get('/api/board/')
        assert r.status_code == status_code

    @pytest.fixture
    def create_board(
            self, *, owner: User,
            pm: User = None,
            contributors: list = None,
            preference: BoardPreference = BoardPreference.public.value
    ):
        if pm:
            contributors.append(pm)
        board = Board(name='Test board',
                      owner=owner,
                      preference=preference)
        if contributors:
            board.save()
            board.contributors.set(contributors)
        board.save()
        return board
