from core.services.file_system import LocalFileSystemServices


class FileSystemProvider:

    def __init__(self, storage):
        if storage == 'LOCAL':
            self.provider = LocalFileSystemServices()
