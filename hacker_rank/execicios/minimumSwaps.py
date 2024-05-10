# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays


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
def minimumSwaps(arr):
    count = 0
    index_dict = {value: index for index, value in enumerate(arr)}

    for i in range(len(arr)):
        if i + 1 != arr[i]:
            index = index_dict[i + 1]
            arr[i], arr[index] = arr[index], arr[i]
            index_dict[arr[i]], index_dict[arr[index]] = i, index
            count += 1
            
    return count