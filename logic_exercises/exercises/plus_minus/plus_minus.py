# https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one

# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.

def plusMinus(arr):
    negative = 0
    positive = 0
    neutral = 0
        
    for element in arr:
        
        if element < 0:
            negative += 1
        
        if element > 0:
            positive += 1
        
        if element == 0:
            neutral += 1
    
    ratio_negative = round(float(negative / len(arr)), 6)
    ratio_positive = round(float(positive / len(arr)), 6)
    ratio_neutral = round(float(neutral / len(arr)), 6)
    
    print(ratio_positive)
    print(ratio_negative)
    print(ratio_neutral)