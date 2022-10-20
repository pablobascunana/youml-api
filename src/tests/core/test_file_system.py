import os

import pytest
from django.conf import settings

from core.managers.file import LocalFileManager
from core.providers.file_system import FileManagerProvider


@pytest.mark.django_db
class TestLocalFileSystem:

    def test_provider(self):
        file_manager = FileManagerProvider(os.getenv('STORAGE_TYPE')).provider
        assert isinstance(file_manager, LocalFileManager)

    def test_exist_path(self):
        file_manager = FileManagerProvider(os.getenv('STORAGE_TYPE')).provider
        exists = file_manager.exist_path(settings.BASE_DIR)
        assert exists

    def test_not_exist_path(self):
        file_manager = FileManagerProvider(os.getenv('STORAGE_TYPE')).provider
        exists = file_manager.exist_path(f'{settings.BASE_DIR}/folder')
        assert not exists

    def test_create_directory(self, tmp_path):
        file_manager = FileManagerProvider(os.getenv('STORAGE_TYPE')).provider
        file_manager.create_directory(tmp_path)
        assert file_manager.exist_path(tmp_path)

    def test_create_path(self, tmp_path):
        file_manager = FileManagerProvider(os.getenv('STORAGE_TYPE')).provider
        full_path = file_manager.create_path(tmp_path, 'abc', 'def')
        assert file_manager.exist_path(full_path)

    def test_format_filename(self):
        file_manager = FileManagerProvider(os.getenv('STORAGE_TYPE')).provider
        filename = file_manager.format_filename('my file.txt')
        assert filename == 'my_file.txt'

    def test_save_file(self, tmp_path):
        filename = '.env.production'
        file_manager = FileManagerProvider(os.getenv('STORAGE_TYPE')).provider
        file_bytes = file_manager.retrieve_file(f'{settings.BASE_DIR}/{filename}')
        file_manager.save_file(f'{tmp_path}/{filename}', file_bytes)
        assert file_manager.exist_path(f'{tmp_path}/{filename}')

    def test_retrieve_file(self):
        filename = '.env.production'
        file_manager = FileManagerProvider(os.getenv('STORAGE_TYPE')).provider
        file_bytes = file_manager.retrieve_file(f'{settings.BASE_DIR}/{filename}')
        assert isinstance(file_bytes, bytes)

    def test_delete_file(self, tmp_path):
        filename = '.env.production'
        file_manager = FileManagerProvider(os.getenv('STORAGE_TYPE')).provider
        file_bytes = file_manager.retrieve_file(f'{settings.BASE_DIR}/{filename}')
        file_manager.save_file(f'{tmp_path}/{filename}', file_bytes)
        file_manager.delete_file(f'{tmp_path}/{filename}')
        assert not file_manager.exist_path(f'{tmp_path}/{filename}')
