#https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

# primeira versão
def merge_the_tools_v1(string, k):
    # your code goes here
    
    len_result = int(len(string)/k)
    dict_slice_str = {}
    slice_str = 0
    
    for item in range(len_result):
        dict_slice_str[f"string{item}"] = string[slice_str:(slice_str+k)]
        slice_str+= k
  
    for key, value in dict_slice_str.items():
        new_str = ""
        
        for value in dict_slice_str[key]:
            if value not in new_str:
                new_str = new_str+value
                       
        dict_slice_str[key] = new_str
        
        print(dict_slice_str[key])

# segunda versão
def merge_the_tools_v2(string, k):
    # your code goes here
    
    len_result = int(len(string)/k)
    index_slice_str = 0

    for item in range(len_result):
        new_str = ""
        new_str = string[index_slice_str:(index_slice_str + k)]
        index_slice_str += k
        
        print_string = ""
         
        for item in range(len(new_str)):
            if new_str[item] not in print_string:
                print_string = print_string + new_str[item]
        
        print(print_string)
        


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools_v1(string, k)