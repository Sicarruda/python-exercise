from datetime import datetime
import sys
from algoritmos.utils.unordered_arrays import *
from algoritmos.utils.ordenation_check import *
print("3",sys.path)

# dd/mm/YY H:M:S:f
format_date = "%d/%m/%Y %H:%M:%S:%f"

# exibe a diferença entre o tempo de inicio e o fim da execução 
def time_diff(start, finish, array):
    diff = finish - start
    msg = f'Array com {array} elementos. Tempo de execução {diff}'

    return msg

# executa o algoritmo e devolve o tempo de execução e o teste
def compare_ordering_time(list_comparation, algorithm):
    for item in list_comparation:
        list_unordered = create_unordered_array(item)

        # Objeto datetime contem o a data e a hora atual
        time_start = datetime.now()
        format_string = time_start.strftime(format_date)
        print("Data inicio = ", format_string)

        array_ordered = algorithm(list_unordered)

        time_finish = datetime.now()
        format_string_2 = time_finish.strftime(format_date)
        print("Data fim = ",format_string_2)

        print(time_diff(time_start, time_finish, item))
        
        ordering_check(array_ordered)