# https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two

# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.

def lonelyinteger(a):
    dict_numbers = {}
    
    for item in a:
        
        if item not in dict_numbers: # if dict_numbers[item] is Null:
            dict_numbers[item] = 1
        else:
            dict_numbers[item] += 1
    
    for number in dict_numbers:
        
        if dict_numbers[number] == 1:
            return number