# ordena o array
def insertion_sort(array):

    control = 0

    while control < len(array):

        if control+1 < len(array):

            if array[control] > array[control + 1]:
                big = array[control]
                array[control] = array[control + 1]
                array[control + 1] = big            

            for i in range(control+1,-1,-1):
                if i != 0:
                    if array[i] < array[i-1]:
                        small = array[i]
                        array[i]=array[i-1]
                        array[i-1]=small

        control += 1
    return array


# TODO fazer insertion_sort com list compreension