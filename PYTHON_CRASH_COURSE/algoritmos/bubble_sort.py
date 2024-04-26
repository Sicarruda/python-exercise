import random
from datetime import datetime


bubble_sort_test_list = [10000]

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

    # random.shuffle(unordered_array) # embaralha um array já existente

    return unordered_array


def bubble_sort_list_comprehension(array):
    [
        [
            # remover o elemento na posição j da lista e, em seguida, inseri-lo na próxima posição (j + 1).
            array.insert(j + 1, array.pop(j))
            for j in range(i) if array[j] > array[j + 1]
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


# exibe a diferença entre o tempo de inicio e o fim da execução
def time_diff(start, finish, array):
    diff = finish - start
    msg = f"Array com {array} elementos. Tempo de execução {diff}"

    return msg


# array_original = create_unordered_array(100)
# # print("ARRAY ORIGINAL",array_original)
# bubble_sort(array_original)
# # print("ARRAY ORDENADO",array_original)


def test_ordenation(array):
    wrong_array = []

    for item in range(len(array)):
        if item > 0 and array[item] < array[item - 1]:
            wrong_array.append(array[item])
        if item < len(array) - 1 and array[item] > array[item + 1]:
            wrong_array.append(array[item])

    if wrong_array:
        print("CÓDIGO ERRADO!!  ARRAY DE ERROS : ", wrong_array)
    else:
        print(f"TESTE EXECUTADO COM SUCESSO: ARRAY DE {len(array)} ELEMENTOS")


def compare_ordering_time(list_comparation):
    for item in list_comparation:
        list_unordered = create_unordered_array(item)

        # Objeto datetime contem o a data e a hora atual
        time_start = datetime.now()
        format_string = time_start.strftime(format_date)
        print("Data inicio = ", format_string)

        array_ordered = bubble_sort_list_comprehension(list_unordered)
        # array_ordered=bubble_sort(list_unordered)

        time_finish = datetime.now()
        format_string_2 = time_finish.strftime(format_date)
        print("Data fim = ", format_string_2)

        print(time_diff(time_start, time_finish, item))

        test_ordenation(bubble_sort(array_ordered))


compare_ordering_time(bubble_sort_test_list)

# print(bubble_sort_list_comprehension([3, 6, 5, 8, 9, 6, 4, 8, 7, 1, 2, 6]))

# test_ordenation([1,2,3,4,5,6,7,8,9])

# TODO como funciona o range? ele é pesado pra gerar uma sequencia de 1 trilhão?
# TODO implementar list comprehesion no bubble sort e comparar com for convencinal
