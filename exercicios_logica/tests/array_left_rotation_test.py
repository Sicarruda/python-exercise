import pytest

import sys
sys.path.append('../exercicios_logica')

# Agora importe o módulo
from exercicios_logica import execicios
from execicios import array_left_rotation as alr


def test_return_array_rotated():
    arr =  [1, 2, 3, 4, 5]

    alr.rotLeft(arr, 2)
    assert arr == [3,4,5,1,2]

    arr =  [1, 2, 3, 4, 5]
    arr_rotated2 = alr.rotLeft(arr, 0)
    assert arr_rotated2 == arr

    arr =  [1, 2, 3, 4, 5]
    arr_rotated3 = alr.rotLeft(arr,7)
    assert arr_rotated3 == [3,4,5,1,2]

retcode = pytest.main()

