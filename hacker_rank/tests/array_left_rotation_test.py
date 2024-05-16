from execicios.array_left_rotation import *


arr = [1, 2, 3, 4, 5]
num_list = [2, 0, 10]
arr_change = [3, 4, 5, 1, 2]


def test_return_array_rotated():
    for num in num_list:
        arr_rotated = rotLeft(arr, num)
        
        if num == 0:
            assert arr_rotated == arr

        assert arr_rotated == arr_change



