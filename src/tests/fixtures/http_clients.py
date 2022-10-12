import pytest

from rest_framework.test import APIClient
from typing import Tuple

from users.models import User


@pytest.fixture
def client_as_admin(user_admin: User) -> Tuple[APIClient, User]:
    client = APIClient()
    client.force_login(user_admin)
    return client, user_admin


@pytest.fixture
def client_as_user(user: User) -> Tuple[APIClient, User]:
    client = APIClient()
    client.force_login(user)
    return client, user


@pytest.fixture
def client_as_inactive_user(inactive_user: User) -> Tuple[APIClient, User]:
    client = APIClient()
    client.force_login(inactive_user)
    return client, inactive_user


@pytest.fixture
def client() -> APIClient:
    return APIClient()
