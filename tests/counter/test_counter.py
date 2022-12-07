from src.pre_built.counter import count_ocurrences

# Resolução desenvolvida com o auxílio dos instrutores de Ciência
# da Computação: Marco Mialaret Júnior e Rodrigo Coin Curvo

FILE_PATH = "data/jobs.csv"


def test_counter():
    assert count_ocurrences(FILE_PATH, "Python") == 1639
    assert count_ocurrences(FILE_PATH, "python") == 1639
    assert count_ocurrences(FILE_PATH, "PYTHON") == 1639
    assert count_ocurrences(FILE_PATH, "Javascript") == 122
    assert count_ocurrences(FILE_PATH, "JavaScriPt") == 122
    assert count_ocurrences(FILE_PATH, "salário") == 0
    assert count_ocurrences(FILE_PATH, "título") == 0
