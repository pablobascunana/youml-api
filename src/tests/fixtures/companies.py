import pytest

from model_bakery import baker

from api.viewsets.company.model import Company
from users.models import User


@pytest.fixture()
def company() -> Company:
    return baker.make(Company, name="Company Name", email="admin@email.com", cif="C12571311")


@pytest.fixture
def company_user() -> User:
    return baker.make(User, email="user@email.com", username="user", name="user", lastname="user",
                      password="fake_password", role="NORMAL")
