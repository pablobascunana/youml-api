import os


class LocalFileSystemServices:

    def __init__(self):
        path = os.getenv('STORAGE_PATH')
        if not self.exist_path(path):
            self.create_directory(path)

    @staticmethod
    def exist_path(path):
        return os.path.exists(path)

    def create_directory(self, path):
        if not self.exist_path(path):
            os.makedirs(path)

    def create_path(self, *args) -> str:
        full_path = os.path.join(os.getenv('STORAGE_PATH'), *args)
        if not self.exist_path(full_path):
            self.create_directory(full_path)
        return full_path

    @staticmethod
    def format_filename(filename: str) -> str:
        return filename.replace(' ', '_')

    @staticmethod
    def save_file(filepath: str, file: bytes):
        with open(filepath, "wb") as f:
            f.write(file)
            f.close()

    @staticmethod
    def retrieve_file(filepath: str) -> bytes:
        with open(filepath, "rb") as f:
            file_bytes = f.read()
            f.close()
        return file_bytes

    def delete_file(self, filepath: str):
        if self.exist_path(filepath):
            os.remove(filepath)
