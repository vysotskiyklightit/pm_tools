import uuid

import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.fixture
def test_password():
    return 'strong-test-pass'


@pytest.fixture
@pytest.mark.django_db(transaction=True)
def create_user(db, django_user_model, test_password, **kwargs):
    kwargs['password'] = test_password
    if 'username' not in kwargs:
        kwargs['username'] = str(uuid.uuid4())
    return django_user_model.objects.create_user(**kwargs)


@pytest.fixture
def auth_header(api_client, username, test_password):
    response = api_client.post(reverse('token_obtain_pair'),
                               data={'username': username,
                                     'password': test_password})
    try:
        header = {'HTTP_AUTHORIZATION': f'Bearer {response.json()["access"]}'}
    except KeyError:
        raise Exception(f'Cannot auth, check credential.'
                        f' Response {response.status_code}')
    return header


@pytest.fixture
def api_client():
    client = APIClient()
    yield client


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
