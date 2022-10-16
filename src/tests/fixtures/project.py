import pytest
from model_bakery import baker

from api.viewsets import Project


@pytest.fixture()
def project() -> Project:
    return baker.make(Project)



