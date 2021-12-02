import pytest
from board.config.common import BoardPreference
from board.models import Board, Column, Ticket, TicketComment
from board.tests.api_tests import scenarios
from django.contrib.auth.models import User

list_owner_public = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'pm_board',
    'board_preference': BoardPreference.public.value,
    'len_response': 4
}
list_owner_private = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'pm_board',
    'board_preference': BoardPreference.private.value,
    'len_response': 4
}
list_contrib_private = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'some_person',
    'board_preference': BoardPreference.private.value,
    'len_response': 4
}
list_user_private = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'test_user',
    'board_preference': BoardPreference.private.value,
    'len_response': 1
}


class TestTicketCommentsPermissionsApi(object):
    scenarios = {
        'test_get_list': (
            list_owner_public,
            list_owner_private,
            list_contrib_private,
            list_user_private
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
        board = self.create_board(owner=create_pm,
                                  contributors=create_contribs,
                                  preference=board_preference)
        column = self.create_column(board_id=board.id)
        ticket = self.create_ticket(column_id=column.id)
        self.create_ticket_comment(
            ticket.id,
            owner_id=create_contribs[0].id)
        api_client.credentials(**auth_header)
        r = api_client.get(
            f'/api/board/{board.id}/column/{column.id}/'
            f'ticket/{ticket.id}/comment/'
        )
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
        column = self.create_column(board_id=board.id)
        ticket = self.create_ticket(column_id=column.id)
        ticket_comment = self.create_ticket_comment(
            ticket.id,
            owner_id=create_contribs[0].id)
        api_client.credentials(**auth_header)
        r = api_client.get(
            f'/api/board/{board.id}/column/{column.id}/'
            f'ticket/{ticket.id}/comment/{ticket_comment.id}/'
        )
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
        column = self.create_column(board_id=board.id)
        ticket = self.create_ticket(column_id=column.id)
        ticket_comment = self.create_ticket_comment(
            ticket.id,
            owner_id=create_contribs[0].id)
        api_client.credentials(**auth_header)
        data = {
            'message': 'my message'
        }
        r = api_client.put(
            f'/api/board/{board.id}/column/{column.id}/'
            f'ticket/{ticket.id}/comment/{ticket_comment.id}/',
            data=data)
        assert r.status_code == status_code
        if status_code == 200:
            ticket_message = r.json()['message']
            assert ticket_message != ticket_comment.message

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
        column = self.create_column(board_id=board.id)
        ticket = self.create_ticket(column_id=column.id)
        ticket_comment = self.create_ticket_comment(
            ticket.id,
            owner_id=create_contribs[0].id)
        api_client.credentials(**auth_header)
        r = api_client.delete(
            f'/api/board/{board.id}/column/{column.id}/'
            f'ticket/{ticket.id}/comment/{ticket_comment.id}/'
        )
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
        board = self.create_board(owner=create_pm,
                                  contributors=create_contribs,
                                  preference=board_preference)
        column = self.create_column(board_id=board.id)
        ticket = self.create_ticket(column_id=column.id)
        data = {
            'message': 'new descript',
        }
        api_client.credentials(**auth_header)
        r = api_client.post(
            f'/api/board/{board.id}/column/{column.id}/'
            f'ticket/{ticket.id}/comment/',
            data=data
        )
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

    def create_column(self, board_id):
        column = Column(name='Test column', board_id=board_id)
        column.save()
        return column

    def create_ticket(self, column_id):
        ticket = Ticket(column_id=column_id,
                        name='Test column',
                        description='Test description',
                        )
        ticket.save()
        return ticket

    def create_ticket_comment(self, ticket_id, owner_id):
        ticket_comment = TicketComment(ticket_id=ticket_id,
                                       message='Test message',
                                       owner_id=owner_id)
        ticket_comment.save()
        return ticket_comment
