#https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    my_list = []
    
    for item in range(N):
        arguments = input()
        arguments_list = arguments.split()
        
        if "print" in arguments_list:
            print(my_list)
        if "insert" in arguments_list:
            my_list.insert(int(arguments_list[1]), int(arguments_list[2]))
        if "remove" in arguments_list:
            my_list.remove(int(arguments_list[1]))
        if "append" in arguments_list:
            my_list.append(int(arguments_list[1]))
        if "sort" in arguments_list:
            my_list.sort()
        if "pop" in arguments_list:
            my_list.pop(-1)
        if "reverse" in arguments_list:
            my_list.reverse()