import pytest
from board.models import Board
from board.tests.api_tests import scenarios
from common.constants import BoardPreference
from django.contrib.auth.models import User


class TestBoardPermissionsApi(object):
    scenarios = {
        'test_get_list': (
            scenarios.list_owner_public,
            scenarios.list_owner_private,
            scenarios.list_contrib_private,
            scenarios.list_user_private
        ),
        'test_get': (
            scenarios.get_owner_public,
            scenarios.get_owner_private,
            scenarios.get_contrib_private,
            scenarios.get_user_private
        ),
        'test_put': (
            scenarios.put_owner_public,
            scenarios.put_owner_private,
            scenarios.put_user_private
        ),
        'test_delete': (
            scenarios.delete_owner_public,
            scenarios.delete_owner_private,
            scenarios.delete_user_private
        ),
        'test_post': (
            scenarios.post_pm,
            scenarios.post_user
        )

    }

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
        create_pm.save()
        print(create_pm.groups.all(), create_pm.id)
        api_client.credentials(**auth_header)
        r = api_client.post('/api/board/', data=data)
        assert r.status_code == status_code

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
