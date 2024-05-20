# import sys
# import os
import pytest

from python_crash_couse.exercicios.list_comprehension import *

# # Obtém o diretório pai do diretório atual duas vezes para chegar ao diretório 'exercicios'
# exercicios_dir = os.path.abspath(
#     os.path.join(os.path.dirname(__file__), "..", "exercicios")
# )
# sys.path.append(exercicios_dir)

# # Agora você pode importar o módulo desejado
# import list_comprehension as lc


def test_return_list_odd_and_pair_numbers():
    lists_odd_and_pair_numbers = odd_and_pair_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert lists_odd_and_pair_numbers == ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])


def test_return_places_with_specific_letter():
    list_places_with_specific_letter = places_with_specific_letter(
        ["Guarulhos", "São Paulo", "Santo André"], "g"
    )
    assert list_places_with_specific_letter == ("g", ["Guarulhos"])


def test_return_capital_title_names():
    list_names_change = capital_title_names(["ana", "carlos", "vitor hugo"])
    assert list_names_change == (
        ["Ana", "Carlos", "Vitor hugo"],
        ["Ana", "Carlos", "Vitor Hugo"],
    )


retcode = pytest.main()
