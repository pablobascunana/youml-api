import pytest
from unittest.mock import MagicMock


@pytest.fixture
def rabbitmq_connection() -> MagicMock:
    return MagicMock()
