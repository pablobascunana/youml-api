import pytest
from model_bakery import baker

from api.viewsets.image.model import Image


@pytest.fixture()
def image() -> Image:
    return baker.make(Image)
