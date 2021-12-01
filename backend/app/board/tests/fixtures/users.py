from typing import List

import pytest
from board.config.common import SystemUsers
from django.contrib.auth.models import Group, User

PASSWORD = 'strong-test-pass'


def get_user(django_user_model, test_password, username, **kwargs) -> User:
    user_obj = django_user_model.objects.filter(username=username)
    if not user_obj.exists():
        kwargs['password'] = test_password
        kwargs['username'] = username
        return django_user_model.objects.create_user(**kwargs)
    return user_obj.first()


@pytest.fixture
def test_password():
    return PASSWORD


@pytest.fixture
def pm_group():
    return SystemUsers.managers.value


@pytest.fixture
def create_pm_group(pm_group):
    group = Group.objects.filter(name=pm_group)
    if not group.exists():
        group = Group(name=pm_group)
        group.save()
    return group


@pytest.fixture
@pytest.mark.django_db(transaction=True)
def user(db, django_user_model, test_password, username, **kwargs) -> User:
    return get_user(django_user_model, test_password, username, **kwargs)


@pytest.fixture
@pytest.mark.django_db(transaction=True)
def create_pm(django_user_model, pm_username, test_password,
              create_pm_group: Group, **kwargs):
    user = get_user(django_user_model, test_password, pm_username, **kwargs)
    if create_pm_group not in user.groups.all():
        user.groups.add(create_pm_group.pk)
        user.save()
    return user


@pytest.fixture
@pytest.mark.django_db(transaction=True)
def create_contribs(django_user_model,
                    contrib_usernames: List[str],
                    test_password):
    contribs = []
    for username in contrib_usernames:
        contribs.append(get_user(django_user_model, test_password, username))
    return contribs
