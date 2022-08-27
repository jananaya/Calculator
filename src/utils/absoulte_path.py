import os


def get_absoulte_path(file, path):
    current_file_path = os.path.dirname(file)
    return os.path.join(current_file_path, path)
