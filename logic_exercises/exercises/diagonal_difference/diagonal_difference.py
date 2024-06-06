# https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two

# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.


def diagonalDifference(arr):
    arr_left_right = []
    arr_right_left = []
    inverse_index = len(arr)-1
    differrence = 0
    
    for item in range(len(arr)):
        arr_left_right.append(arr[item][item])
        arr_right_left.append(arr[item][inverse_index-item])
    
    sum_left_right = sum(arr_left_right)
    sum_right_left = sum(arr_right_left)
  
    if sum_left_right > sum_right_left:
        differrence = sum_left_right - sum_right_left
    else:
        differrence = sum_right_left - sum_left_right
        
    return differrence