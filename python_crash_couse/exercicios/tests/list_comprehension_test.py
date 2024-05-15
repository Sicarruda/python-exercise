import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import list_comprehension as lc


list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pair_list = [2, 4, 6, 8, 10]
odd_list = [1, 3, 5, 7, 9]
list_names = ["ana", "carlos", "vitor hugo"]
list_capital_names = ["Ana", "Carlos", "Vitor hugo"]
list_title_names = ["Ana", "Carlos", "Vitor Hugo"]
list_places = ["Guarulhos", "São Paulo", "Santo André"]
letter = "g"

def test_return_list_odd_and_pair_numbers():
    lists_odd_and_pair_numbers = lc.odd_and_pair_numbers(list_numbers)
    assert lists_odd_and_pair_numbers == (pair_list, odd_list)

def test_return_places_with_specific_letter():
    list_places_with_specific_letter = lc.places_with_specific_letter(
        list_places, letter
    )
    assert list_places_with_specific_letter == (letter, ["Guarulhos"])

def test_return_capital_title_names():
    list_names_change = lc.capital_title_names(list_names)
    assert list_names_change == (list_capital_names, list_title_names)
