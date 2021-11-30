import pytest
from board.config.common import BoardPreference
from board.models import Board
from django.contrib.auth.models import User


class TestBoardApi(object):
    scenarios = [
        ('Owner get public', {
            'username': 'test_user',
            'pm_username': 'pm_board',
            'contrib_usernames': ['pm_board', 'some_person'],
            'auth_username': 'pm_board',
            'board_preference': BoardPreference.public.value,
            'status_code': 200,
            'len_response': 1}),
        ('Owner get private', {
            'username': 'test_user',
            'pm_username': 'pm_board',
            'contrib_usernames': ['pm_board', 'some_person'],
            'auth_username': 'pm_board',
            'board_preference': BoardPreference.private.value,
            'status_code': 200,
            'len_response': 1}),
        ('Contrib get private', {
            'username': 'test_user',
            'pm_username': 'pm_board',
            'contrib_usernames': ['pm_board', 'some_person'],
            'auth_username': 'some_person',
            'board_preference': BoardPreference.private.value,
            'status_code': 200,
            'len_response': 1}),
        ('User get private', {
            'username': 'test_user',
            'pm_username': 'pm_board',
            'contrib_usernames': ['pm_board', 'some_person'],
            'auth_username': 'test_user',
            'board_preference': BoardPreference.private.value,
            'status_code': 403,
            'len_response': 0}),

    ]

    @pytest.mark.django_db(transaction=True)
    def test_get_list(
            self,
            api_client,
            user,
            create_pm,
            create_contribs,
            auth_header,
            board_preference,
            status_code,
            len_response,
    ):
        self.create_board(owner=create_pm,
                          contributors=create_contribs,
                          preference=board_preference)
        api_client.credentials(**auth_header)
        r = api_client.get('/api/board/')
        assert len(r.json()) == len_response

    @pytest.mark.django_db(transaction=True)
    def test_get(
            self,
            api_client,
            user,
            create_pm,
            create_contribs,
            auth_header,
            board_preference,
            status_code,
            len_response,
    ):
        board = self.create_board(owner=create_pm,
                                  contributors=create_contribs,
                                  preference=board_preference)
        api_client.credentials(**auth_header)
        r = api_client.get(f'/api/board/{board.id}/')
        assert r.status_code == status_code

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
