import pytest
from model_bakery import baker

from api.viewsets.dataset.model import Dataset


@pytest.fixture()
def dataset() -> Dataset:
    return baker.make(Dataset)
