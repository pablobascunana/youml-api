import os

import pytest

from core.managers.file import LocalFileManager
from core.providers.file_system import FileManagerProvider


@pytest.fixture()
def file_manager() -> LocalFileManager:
    return FileManagerProvider(os.getenv('STORAGE_TYPE')).provider
