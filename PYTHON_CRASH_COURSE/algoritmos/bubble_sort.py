import random
from datetime import datetime


bubble_sort_test_list = [10,100,1000,10000]
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

    # random.shuffle(unordered_array) embaralha um array já existente

    return unordered_array

# ordena o array
def bubble_sort(array):
    array_length = len(array)
    
    while array_length > 1:

        for i in range(array_length):

            if (i+1) < array_length:

                if array[i] > array[i+1]:
                    bigger = array[i]
                    array[i] = array[i+1]
                    array[i+1] = bigger

            else:
                array_length -= 1
                continue

# exibe a diferença entre o tempo de inicio e o fim da execução 
def time_diff(start, finish, array):
    diff = finish - start
    msg = f'Array com {array} elementos. Tempo de execução {diff}'

    return msg

# array_original = create_unordered_array(100)
# # print("ARRAY ORIGINAL",array_original)
# bubble_sort(array_original)
# # print("ARRAY ORDENADO",array_original)


def compare_ordering_time(list_comparation):
    for item in list_comparation:
        list_unordered = create_unordered_array(item)

        # Objeto datetime contem o a data e a hora atual
        time_start = datetime.now()
        format_string = time_start.strftime(format_date)
        print("Data inicio = ", format_string)

        bubble_sort(list_unordered)

        time_finish = datetime.now()
        format_string_2 = time_finish.strftime(format_date)
        print("Data fim = ",format_string_2)

        print(time_diff(time_start, time_finish, item))
    

compare_ordering_time(bubble_sort_test_list)

def test_ordenation(array):
    pass





# tempo em ms -ok
# varias ordenações com 10, 100, 1000, 10000 e 1000000 elementos e imprimir o tempo que demorou cada uma. Comparar a evolução do tempo com o tamanho do array - ok 
# usar valores aleatórios no array - ok
# melhorar nomes das variaveis - ok
# Tentar implementar outra copia dessa função sem usar range! Tenta manipular os indices dentro do for - ok
# como funciona o range? ele é pesado pra gerar uma sequencia de 1 trilhão?
# função para verificar se um array está ordenado 
