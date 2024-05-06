"""
    Dado um Número n, diga se ele é palindromo com e sem converter para string
"""

num1 = 12321
num2 = 12341

def palindromo_str(num):
    str_num = str(num)
    reverse_str_num = str_num[::-1]
    if reverse_str_num == str_num:
        return True
    
    return False

print(palindromo_str(num1))
print(palindromo_str(num2))


def palindromo_sem_str(num):
    pass