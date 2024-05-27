# https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.

# imput = [
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6],
# ]


def hourglassSum(arr):
    top = 0
    middle = 0
    botton = 0
    sum_line = []

    for line in range(4):

        for element in range(4):

            top = arr[line][element] + arr[line][element + 1] + arr[line][element + 2]
            middle = arr[line + 1][element + 1]
            botton = arr[line + 2][element] + arr[line + 2][element + 1]+ arr[line + 2][element + 2]

            sum_line.append(top + middle + botton)

    sum_line.sort()

    return sum_line[-1]
