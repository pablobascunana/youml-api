from core.managers.file import LocalFileManager


class FileManagerProvider:

    def __init__(self, storage):
        if storage == 'LOCAL':
            self.provider = LocalFileManager()
