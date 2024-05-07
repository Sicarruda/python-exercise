from time_comparer import *

cocktail_sort_test_list = [10, 100, 1000]

def cocktail_sort(array):
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