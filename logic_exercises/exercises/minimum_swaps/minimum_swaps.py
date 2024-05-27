# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# meu codigo
def minimumSwaps(arr):
    count = 0

    for i in range(len(arr)):

        if i + 1 != arr[i]:
            index = arr.index(i + 1)
            change = arr[i]
            arr[i] = arr[index]
            arr[index] = change
            count += 1

    return count


# Código otimizado pelo Chat-GPT 
# o arr.index é o responsavel por aumentar o tempo de execução, usamos um dict com list comprehesion para gravar os valores e index e assim a busca fica mais rapida.
def minimumSwaps_GPT(arr):
    count = 0
    index_dict = {value: index for index, value in enumerate(arr)}

    for i in range(len(arr)):
        if i + 1 != arr[i]:
            index = index_dict[i + 1]
            arr[i], arr[index] = arr[index], arr[i]
            index_dict[arr[i]], index_dict[arr[index]] = i, index
            count += 1
            
    return count

"""
Chat-GPT:

    Código Original:
        O loop for percorre o array uma vez, o que é uma operação de O(n), onde 'n' é o tamanho do array.
        Dentro do loop, a função index() é chamada para encontrar o índice do elemento que precisa ser trocado. Isso tem uma complexidade de O(n) no pior caso, pois a função index() precisa percorrer o array até encontrar o elemento.
        Portanto, a complexidade total do código original é de O(n^2), devido ao loop externo e ao uso da função index() dentro do loop.

    Código Corrigido:
        Assim como o código original, o loop for percorre o array uma vez, o que ainda é uma operação de O(n).
        No entanto, dentro do loop, o acesso aos índices no dicionário index_dict é uma operação de O(1), já que os dicionários em Python têm acesso rápido aos valores por chave.
        Portanto, a complexidade total do código corrigido é de O(n), pois a complexidade dominante é determinada pelo loop externo.

    Em resumo, o código corrigido é significativamente mais eficiente em termos de complexidade de tempo, já que evita a necessidade de buscar índices dentro do loop, reduzindo a complexidade total para O(n).
"""