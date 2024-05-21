# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d

def rotLeft(a, d):
    print("INICIO",a, d)
    while d > 0:
        print("WHILE",a, d)
        index = 0
        a.append(a[index])
        a.pop(index)
        d -= 1
        index += 1
        
    print("RESULT",a, d)
    return a

# print(rotLeft([1, 2, 3, 4, 5],2))