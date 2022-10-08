def read_file(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read()


def replace_keys(template: str, key: str, value: str) -> str:
    return template.replace(key, value)
