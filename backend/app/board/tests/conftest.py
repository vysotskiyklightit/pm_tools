import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from .fixtures import *


@pytest.fixture
def api_client():
    client = APIClient()
    yield client


@pytest.fixture
def auth_header(api_client, auth_username, test_password):
    response = api_client.post(reverse('token_obtain_pair'),
                               data={'username': auth_username,
                                     'password': test_password})
    try:
        header = {'HTTP_AUTHORIZATION': f'Bearer {response.json()["access"]}'}
    except KeyError:
        raise Exception(f'Cannot auth, check credential.'
                        f' Response {response.status_code}')
    return header


def pytest_generate_tests(metafunc):
    idlist = []
    argvalues = []
    if hasattr(metafunc.cls, 'scenarios'):
        for scenario in metafunc.cls.scenarios:
            idlist.append(scenario[0])
            items = scenario[1].items()
            argnames = [x[0] for x in items]
            argvalues.append([x[1] for x in items])
        metafunc.parametrize(argnames, argvalues, ids=idlist, scope='class')
