import pytest
import requests_mock
from django.conf import settings


@pytest.fixture
def mock_success_post():
    with requests_mock.Mocker() as requests_mocker:
        requests_mocker.post(f"{settings.MANAGER_URL}/train", status_code=200)
        yield


@pytest.fixture
def mock_forbidden_post():
    with requests_mock.Mocker() as requests_mocker:
        requests_mocker.post(f"{settings.MANAGER_URL}/train", status_code=403)
        yield


@pytest.fixture
def mock_not_found_post():
    with requests_mock.Mocker() as requests_mocker:
        requests_mocker.post(f"{settings.MANAGER_URL}/train", status_code=404)
        yield
