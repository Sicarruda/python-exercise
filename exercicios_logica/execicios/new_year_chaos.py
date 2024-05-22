# https://www.hackerrank.com/challenges/new-year-chaos/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.

def minimumBribes(q):
    bribes_sum = 0
    bribe = 0
    msg = ""
    
    for element in range(len(q)-1):
        bribe = 0
        if q[element] > q[element+1]:
            bribe = q[element] - q[element+1]
            if bribe > 2:
                msg = "Too chaotic"
                break
                
            else:
                bribes_sum = bribes_sum + bribe
    if msg:
        print(msg)
        
    else:
        print(bribes_sum)

minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])

