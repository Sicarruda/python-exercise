"""
    Dado um Número n, diga se ele é palindromo com e sem converter para string
"""

num1 = 12321
num2 = 12341
num3 = 136547898745631


def palindromo_str(num):
    str_num = str(num)
    reverse_str_num = str_num[::-1]
    if reverse_str_num == str_num:
        return True

    return False


def palindromo_str_interavel(num):
    str_num = str(num)
    array_str_num = list(str_num)
    len_array = len(array_str_num) - 1
    palindromo = True

    for i in range(len_array):

        if array_str_num[i] != array_str_num[len_array - i]:
            palindromo = False
            break

    return palindromo


# https://pt.stackoverflow.com/questions/559104/verificar-se-o-n%C3%BAmero-%C3%A9-pal%C3%ADndromo-em-c-sem-usar-vetor


def palindromo_sem_str(num):
    numero = num % 10
    palindromo = 0
    palindromo = palindromo * 10 + numero
    
    pass


print(palindromo_str_interavel(num1))
print(palindromo_str_interavel(num2))
print(palindromo_str_interavel(num3))
