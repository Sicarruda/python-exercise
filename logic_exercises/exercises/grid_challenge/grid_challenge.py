# https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four

# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.


# My Response

def gridChallenge(grid):
    new_grid = []
    len_grid = len(grid)
    
    for line in grid:
        ordered_string = ''.join(sorted(line))
        new_grid.append(ordered_string)
        
    # index column
    for column in range(len(new_grid[0])):
        # index line
        for line in range(len_grid):
            if line+1 < len_grid:
                if new_grid[line][column] > new_grid[line+1][column]:
                    return "NO"
                    
    return "YES"
    
# Hacker rank code
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()