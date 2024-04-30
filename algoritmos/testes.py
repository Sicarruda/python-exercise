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