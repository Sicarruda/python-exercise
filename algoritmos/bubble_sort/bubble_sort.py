import sys
import os
print("1",sys.path)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
print("2",sys.path)
from algoritmos.utils.time_comparer import *


bubble_sort_test_list = [10, 100, 1000, 10000]


def bubble_sort_list_comprehension(array):
    [
        [
            # remover o elemento na posição j da lista e, em seguida, inseri-lo na próxima posição (j + 1).
            array.insert(j + 1, array.pop(j))
            for j in range(i)
            if array[j] > array[j + 1]
        ]
        # o range(len(array) - 1, 0, -1) gera uma sequência de números inteiros começando do
        # penúltimo índice do array, decrementando 1 a cada iteração, até o primeiro índice (0).
        for i in range(len(array) - 1, 0, -1)
    ]

    return array

# ordena o array
def bubble_sort(array):
    array_length = len(array)

    while array_length > 1:

        for i in range(array_length):

            if (i + 1) < array_length:

                if array[i] > array[i + 1]:
                    bigger = array[i]
                    array[i] = array[i + 1]
                    array[i + 1] = bigger

            else:
                array_length -= 1
                continue

    return array

compare_ordering_time(bubble_sort_test_list, bubble_sort)


# TODO como funciona o range? ele é pesado pra gerar uma sequencia de 1 trilhão?
