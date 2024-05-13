"""
    Dado um Número n, diga se ele é palindromo com e sem converter para string
"""

num1 = 12321
num2 = 12341
num3 = 136547898745631
num4 = 11
num5 = 2


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
    original_number = num
    reversed_number = 0
    
    while num > 0:
        digit = num % 10  # Pega o último dígito
        reversed_number = reversed_number * 10 + digit  # Adiciona o dígito ao número invertido
        num = num // 10  # Remove o último dígito do número original
    
    if original_number == reversed_number:
        return True
    
    return False
   


print(palindromo_sem_str(num1))
print(palindromo_sem_str(num2))
print(palindromo_sem_str(num3))
print(palindromo_sem_str(num4))
print(palindromo_sem_str(num5))
