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
    if not hasattr(metafunc.cls, 'scenarios'):
        return
    if metafunc.function.__name__ not in metafunc.cls.scenarios:
        return
    funcarglist = metafunc.cls.scenarios[metafunc.function.__name__]
    argnames = sorted(funcarglist[0])
    argvalues = [[funcargs[name] for name in argnames]
                 for funcargs in funcarglist]
    metafunc.parametrize(argnames, argvalues)
