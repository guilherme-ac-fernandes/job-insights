from src.pre_built.counter import count_ocurrences

# Resolução desenvolvida com o auxílio dos instrutores de Ciência
# da Computação: Marco Mialaret Júnior e Rodrigo Coin Curvo


def test_counter():
    assert count_ocurrences("data/jobs.csv", 'Python') == 1639
    assert count_ocurrences("data/jobs.csv", 'python') == 1639
    assert count_ocurrences("data/jobs.csv", 'PYTHON') == 1639
    assert count_ocurrences("data/jobs.csv", 'Javascript') == 122
    assert count_ocurrences("data/jobs.csv", 'JavaScriPt') == 122
    assert count_ocurrences("data/jobs.csv", 'salário') == 0
    assert count_ocurrences("data/jobs.csv", 'título') == 0
