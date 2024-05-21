# ordena o array
def selection_sort(array):
    len_array = len(array)

    for i in range(len_array):

        if i < (len_array-1):
        
            for j in range(i+1,len_array):

                if array[i] > array[j]:
                    bigger = array[i]
                    array[i] = array[j]
                    array[j] = bigger

    return array
