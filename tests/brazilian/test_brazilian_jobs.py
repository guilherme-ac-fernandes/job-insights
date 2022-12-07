import random
from src.pre_built.brazilian_jobs import read_brazilian_file


FILE_PATH = 'tests/mocks/brazilians_jobs.csv'

index = random.randint(1, len(read_brazilian_file(FILE_PATH)) - 1)


def test_brazilian_jobs_rename_keys_to_english():
    assert "title" in read_brazilian_file(FILE_PATH)[index]
    assert "salary" in read_brazilian_file(FILE_PATH)[index]
    assert "type" in read_brazilian_file(FILE_PATH)[index]


def test_brazilian_jobs_remove_portuguese_keys():
    assert "titulo" not in read_brazilian_file(FILE_PATH)[index]
    assert "salario" not in read_brazilian_file(FILE_PATH)[index]
    assert "tipo" not in read_brazilian_file(FILE_PATH)[index]


def test_brazilian_jobs():
    assert isinstance(read_brazilian_file(FILE_PATH), list)
    assert isinstance(read_brazilian_file(FILE_PATH)[index], dict)
    test_brazilian_jobs_rename_keys_to_english()
    test_brazilian_jobs_remove_portuguese_keys()
