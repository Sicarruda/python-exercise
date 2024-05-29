import pytest

from array_left_rotation import *


def test_return_array_rotated():
    arr =  [1, 2, 3, 4, 5]

    rotLeft(arr, 2)
    assert arr == [3,4,5,1,2]

    arr =  [1, 2, 3, 4, 5]
    arr_rotated2 = rotLeft(arr, 0)
    assert arr_rotated2 == arr

    arr =  [1, 2, 3, 4, 5]
    arr_rotated3 = rotLeft(arr,7)
    assert arr_rotated3 == [3,4,5,1,2]

retcode = pytest.main()

