import pytest
from django.contrib.auth.hashers import make_password

from model_bakery import baker

from users.models import User


@pytest.fixture()
def user_admin() -> User:
    return baker.make(User, email='admin@email.com', username='user_admin', name='user', lastname='admin',
                      password=make_password('fake_password'), role='ADMIN', active=True)


@pytest.fixture
def user() -> User:
    return baker.make(User, email='user@email.com', username='user', name='user', lastname='user',
                      password=make_password('fake_password'), role='NORMAL')


@pytest.fixture
def inactive_user() -> User:
    return baker.make(User, email='user@email.com', username='user', name='user', lastname='user', verified=True,
                      active=False, login_attempts=5, password=make_password('fake_password'), role='NORMAL')
