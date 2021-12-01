import pytest
from board.config.common import BoardPreference
from board.models import Board
from django.contrib.auth.models import User

list_owner_public = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'pm_board',
    'board_preference': BoardPreference.public.value,
    'len_response': 1
}
list_owner_private = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'pm_board',
    'board_preference': BoardPreference.private.value,
    'len_response': 1
}
list_contrib_private = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'some_person',
    'board_preference': BoardPreference.private.value,
    'len_response': 1
}
list_user_private = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'test_user',
    'board_preference': BoardPreference.private.value,
    'len_response': 0
}
get_owner_public = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'pm_board',
    'board_preference': BoardPreference.public.value,
    'status_code': 200
}
get_owner_private = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'pm_board',
    'board_preference': BoardPreference.private.value,
    'status_code': 200
}
get_contrib_private = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'some_person',
    'board_preference': BoardPreference.private.value,
    'status_code': 200
}
get_user_private = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'test_user',
    'board_preference': BoardPreference.private.value,
    'status_code': 403
}
put_owner_public = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'pm_board',
    'board_preference': BoardPreference.public.value,
    'status_code': 200
}
put_owner_private = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'pm_board',
    'board_preference': BoardPreference.private.value,
    'status_code': 200
}
put_user_private = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'test_user',
    'board_preference': BoardPreference.private.value,
    'status_code': 403
}
delete_owner_public = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'pm_board',
    'board_preference': BoardPreference.public.value,
    'status_code': 204
}
delete_owner_private = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'pm_board',
    'board_preference': BoardPreference.private.value,
    'status_code': 204
}
delete_user_private = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'test_user',
    'board_preference': BoardPreference.private.value,
    'status_code': 403
}

post_pm = {
    'username': 'test_user5',
    'pm_username': 'pm_board1',
    'contrib_usernames': ['pm_board1', 'some_person'],
    'auth_username': 'pm_board1',
    'board_preference': BoardPreference.private.value,
    'status_code': 201
}
post_user = {
    'username': 'test_user5',
    'pm_username': 'pm_board1',
    'contrib_usernames': ['pm_board1', 'some_person'],
    'auth_username': 'test_user5',
    'board_preference': BoardPreference.private.value,
    'status_code': 403
}


class TestBoardPermissionsApi(object):
    scenarios = {
        'test_get_list': (
            list_owner_public,
            list_owner_private,
            list_contrib_private,
            list_user_private
        ),
        'test_get': (
            get_owner_public,
            get_owner_private,
            get_contrib_private,
            get_user_private
        ),
        'test_put': (
            put_owner_public,
            put_owner_private,
            put_user_private
        ),
        'test_delete': (
            delete_owner_public,
            delete_owner_private,
            delete_user_private
        ),
        'test_post': (
            post_pm,
            post_user
        )

    }

    @pytest.mark.django_db(transaction=True)
    def test_get_list(
            self,
            api_client,
            user,
            create_pm,
            create_contribs,
            auth_header,
            board_preference,
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
    ):
        board = self.create_board(owner=create_pm,
                                  contributors=create_contribs,
                                  preference=board_preference)
        api_client.credentials(**auth_header)
        r = api_client.get(f'/api/board/{board.id}/')
        assert r.status_code == status_code

    @pytest.mark.django_db(transaction=True)
    def test_put(
            self,
            api_client,
            user,
            create_pm,
            create_contribs,
            auth_header,
            board_preference,
            status_code,
    ):
        board = self.create_board(owner=create_pm,
                                  contributors=create_contribs,
                                  preference=board_preference)
        api_client.credentials(**auth_header)
        data = {
            'owner': board.owner.pk,
            'contributors': [contrib.id for contrib in
                             board.contributors.all()],
            'name': 'new name',
            'preference': board_preference
        }
        r = api_client.put(f'/api/board/{board.id}/', data=data)
        assert r.status_code == status_code
        if status_code == 200:
            board_name = r.json()['name']
            assert board_name != board.name

    @pytest.mark.django_db(transaction=True)
    def test_delete(
            self,
            api_client,
            user,
            create_pm,
            create_contribs,
            auth_header,
            board_preference,
            status_code,
    ):
        board = self.create_board(owner=create_pm,
                                  contributors=create_contribs,
                                  preference=board_preference)
        api_client.credentials(**auth_header)
        r = api_client.delete(f'/api/board/{board.id}/')
        assert r.status_code == status_code
        if status_code == 200:
            board_name = r.json()['name']
            assert board_name != board.name

    @pytest.mark.django_db(transaction=True)
    def test_post(
            self,
            api_client,
            user,
            create_pm,
            create_contribs,
            auth_header,
            board_preference,
            status_code,
    ):
        data = {
            'preference': board_preference,
            'name': 'new board',
            'contributors': [c.id for c in create_contribs],
        }
        api_client.credentials(**auth_header)
        r = api_client.post('/api/board/', data=data)
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
