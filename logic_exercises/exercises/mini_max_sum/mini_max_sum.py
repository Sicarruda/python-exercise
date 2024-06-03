# https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one

# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.

def miniMaxSum(arr):
    min_sum = 0
    max_sum = 0
    bigger_num = 0
    smaler_num = 0
    
    for num in arr:
        if num > bigger_num:
            bigger_num = num
            
    smaler_num = bigger_num
    
    for num in arr:
        if num < smaler_num:
            smaler_num = num
            
    arr.remove(bigger_num)
    arr.remove(smaler_num)
    
    min_sum = sum(arr) + smaler_num
    max_sum = sum(arr) + bigger_num
    
    print(min_sum, max_sum)

