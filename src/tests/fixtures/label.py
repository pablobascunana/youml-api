import pytest
from model_bakery import baker

from api.viewsets.label.model import Label


@pytest.fixture()
def label() -> Label:
    return baker.make(Label)
