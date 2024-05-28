# https://www.hackerrank.com/challenges/new-year-chaos/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.

# def minimumBribes_meu(q):
#     bribes_sum = 0
#     msg = ""
    
#     for element in range(len(q)-1):
#         bribe = 0

#         if q[element] > q[element+1]:
#             bribe = q[element] - q[element+1]

#             if bribe > 2:
#                 msg = "Too chaotic"
#                 break
#             else:
#                 bribes_sum = bribes_sum + bribe

#     if msg:
#         print(msg)
#     else:
#         print(bribes_sum)


def minimumBribes_novo(q):
    bribes_sum = 0
    max_bribes = 2 
    
    for index in range(len(q)):
        original_position = index+1
        
        x = q[index] - original_position
        
        if  x > max_bribes:
            print("Too chaotic")
            return
        
        start = max(0, q[index] - max_bribes)

        for place in range(start, index, 1):

            if q[place] > q[index]:
                bribes_sum+=1

    print(bribes_sum)
    return 


minimumBribes_novo([1, 2, 5, 3, 7, 8, 6, 4])

