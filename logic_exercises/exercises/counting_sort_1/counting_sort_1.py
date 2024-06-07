# https://www.hackerrank.com/challenges/one-week-preparation-kit-countingsort1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two

# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.

# Tempo O(n) memoria O(n)
 
def countingSort(arr):
    dict_numbers = {}
    new_arr = []
    bigest_arr_number = 100
    
    for item in arr:
        if item not in dict_numbers:
            dict_numbers[item] = 1
        else:
            dict_numbers[item] += 1
            
    for index in range(bigest_arr_number):
        if index in dict_numbers:
            new_arr.append(dict_numbers[index])
        else:
            new_arr.append(0)
            
    return new_arr