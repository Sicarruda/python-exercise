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


def minimumSwaps_sem_for(arr):
    count = 0

    list(filter(lambda x: True if print(x) is None else False, arr))
    pair_list = [item for item in len_arr if i + 1 != arr[i]]