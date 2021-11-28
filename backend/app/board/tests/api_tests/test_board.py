import pytest


class TestBoardApi(object):
    # scenarios = [
    #     ('ERROR', {'username': 'den',
    #                'password': 'admin3458df',
    #                }),
    # ]

    @pytest.mark.django_db(transaction=True)
    def test_get_list(self, api_client, auth_header):
        headers, user = auth_header
        api_client.credentials(**headers)
        r = api_client.get('/api/board/', **headers)
        assert r.status_code == 200
