import random
from datetime import datetime

insertion_sort_test_list = [10, 100, 1000, 10000]
# dd/mm/YY H:M:S:f
format_date = "%d/%m/%Y %H:%M:%S:%f"

# cria o array
def create_unordered_array(array_len):
    unordered_array = []
    created_array = True

    while created_array:
        item = random.randrange(1, array_len)
        unordered_array.append(item)

        if len(unordered_array) == array_len:
            created_array = False

    return unordered_array


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

# exibe a diferença entre o tempo de inicio e o fim da execução 
def time_diff(start, finish, array):
    diff = finish - start
    msg = f'Array com {array} elementos. Tempo de execução {diff}'

    return msg

def compare_ordering_time(list_comparation):
    for item in list_comparation:
        list_unordered = create_unordered_array(item)

        # Objeto datetime contem o a data e a hora atual
        time_start = datetime.now()
        format_string = time_start.strftime(format_date)
        print("Data inicio = ", format_string)

        insertion_sort(list_unordered)

        time_finish = datetime.now()
        format_string_2 = time_finish.strftime(format_date)
        print("Data fim = ",format_string_2)

        print(time_diff(time_start, time_finish, item))

compare_ordering_time(insertion_sort_test_list)
