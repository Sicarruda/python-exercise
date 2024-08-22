"""
    Dado um Número n, diga se ele é palindromo com e sem converter para string
"""

num1 = 12321
num2 = 12341
num3 = 136547898745631
num4 = 11
num5 = 2


def palindrome_str(num):
    try:

        if not num and num != 0:
            raise TypeError("Valor necessário")

        if type(num) != int:
            raise ValueError("Valor numerico necessário")

        str_num = str(num)
        reverse_str_num = str_num[::-1]

        if reverse_str_num == str_num:
            return True

        return False

    except ValueError as e:
        return str(e)

    except TypeError as e:
        return str(e)


def palindrome_str_iterable(num):
    try:

        if not num and num != 0:
            raise TypeError("Valor necessário")

        if type(num) != int:
            raise ValueError("Valor numerico necessário")

        str_num = str(num)
        array_str_num = list(str_num)
        len_array = len(array_str_num) - 1
        palindromo = True

        for i in range(len_array):

            if array_str_num[i] != array_str_num[len_array - i]:
                palindromo = False
                break

        return palindromo

    except ValueError as e:
        return str(e)

    except TypeError as e:
        return str(e)


# https://pt.stackoverflow.com/questions/559104/verificar-se-o-n%C3%BAmero-%C3%A9-pal%C3%ADndromo-em-c-sem-usar-vetor


def palindrome_without_str(num):
    try:

        if not num and num != 0:
            raise TypeError("Valor necessário")

        if type(num) != int:
            raise ValueError("Valor numerico necessário")

        original_number = num
        reversed_number = 0

        while num > 0:
            digit = num % 10  # Pega o último dígito
            reversed_number = (
                reversed_number * 10 + digit
            )  # Adiciona o dígito ao número invertido
            num = num // 10  # Remove o último dígito do número original

        if original_number == reversed_number:
            return True

        return False
    except ValueError as e:
        return str(e)

    except TypeError as e:
        return str(e)


# print(palindrome_without_str(num1))
# print(palindrome_without_str(num2))
# print(palindrome_without_str(num3))
# print(palindrome_without_str(num4))
# print(palindrome_without_str(num5))

def is_palindrome(s):
    reversed_s = s[::-1]

    if reversed_s == s:
        return True
    
    return False

def palindrome_index(s):
    print(s)

    if is_palindrome(s):
        return -1

    left, right = 0, len(s)-1
    
    while left < right-1:
        if s[left] != s[right]:

            # Verifica se remover o caractere da esquerda ou da direita torna a string um palíndromo
            if is_palindrome(s[left + 1:right+1]):
                return left
            
            elif is_palindrome(s[left:right]):
                return right
            
            else:
                return -1
            
        left += 1
        right -= 1
    
    return -1


print(palindrome_index("aaab"))  # 3
print(palindrome_index("baa"))  # 0
print(palindrome_index("aaa"))  # -1
print(palindrome_index("acba"))  # 1
print(palindrome_index("abcda"))  # -1
print(palindrome_index("aabc"))  # -1
