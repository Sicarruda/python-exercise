import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import list_comprehension as lc

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pair_list = [2,4,6,8,10]
odd_list = [1,3,5,7,9]


def test_return_list_odd_and_pair_numbers():
    lists_odd_and_pair_numbers = lc.odd_and_pair_numbers(list_numbers)
    assert lists_odd_and_pair_numbers == (pair_list, odd_list)
    