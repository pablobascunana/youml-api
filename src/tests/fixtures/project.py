import pytest
from model_bakery import baker

from api.viewsets.project.model import Project


@pytest.fixture()
def project(tmp_path) -> Project:
    return baker.make(Project, storage_in=tmp_path)



