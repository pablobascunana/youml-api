import pytest
from django.conf import settings

from core.managers.file import LocalFileManager


@pytest.mark.django_db
class TestLocalFileSystem:

    filename = '.env.production'

    @staticmethod
    def test_provider(file_manager):
        assert isinstance(file_manager, LocalFileManager)

    @staticmethod
    def test_exist_path(file_manager):
        exists = file_manager.exist_path(settings.BASE_DIR)
        assert exists

    @staticmethod
    def test_not_exist_path(file_manager):
        exists = file_manager.exist_path(f'{settings.BASE_DIR}/folder')
        assert not exists

    @staticmethod
    def test_create_directory(file_manager, tmp_path):
        file_manager.create_directory(tmp_path)
        assert file_manager.exist_path(tmp_path)

    @staticmethod
    def test_create_path(file_manager, tmp_path):
        full_path = file_manager.create_path(tmp_path, 'abc', 'def')
        assert file_manager.exist_path(full_path)

    @staticmethod
    def test_format_filename(file_manager):
        filename = file_manager.format_filename('my file.txt')
        assert filename == 'my_file.txt'

    def test_save_file(self, file_manager, tmp_path):
        file_bytes = file_manager.retrieve_file(f'{settings.BASE_DIR}/{self.filename}')
        file_manager.save_file(f'{tmp_path}/{self.filename}', file_bytes)
        assert file_manager.exist_path(f'{tmp_path}/{self.filename}')

    def test_retrieve_file(self, file_manager):
        file_bytes = file_manager.retrieve_file(f'{settings.BASE_DIR}/{self.filename}')
        assert isinstance(file_bytes, bytes)

    def test_delete_file(self, file_manager, tmp_path):
        file_bytes = file_manager.retrieve_file(f'{settings.BASE_DIR}/{self.filename}')
        file_manager.save_file(f'{tmp_path}/{self.filename}', file_bytes)
        file_manager.delete_file(f'{tmp_path}/{self.filename}')
        assert not file_manager.exist_path(f'{tmp_path}/{self.filename}')
