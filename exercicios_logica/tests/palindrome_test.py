import pytest

from exercicios_logica.execicios.palindrome import *


def test_is_palindromo_with_str():
    assert palindrome_str(12321) == True
    assert palindrome_str(1243421) == True
    assert palindrome_str(2) == True
    assert palindrome_str(0) == True
    assert palindrome_str(11) == True
    assert palindrome_str("") == "Valor necessário"
    assert palindrome_str("123") == "Valor numerico necessário"
    assert palindrome_str(123.12) == "Valor numerico necessário"
    assert palindrome_str([1, 2, 3]) == "Valor numerico necessário"
    assert palindrome_str(112) == False
    assert palindrome_str(123456) == False
    assert palindrome_str(11111112) == False
    assert palindrome_str(111111111111111111112) == False

def test_test_is_palindromo_with_str_iteravel():
    assert palindrome_str_iterable(12321) == True
    assert palindrome_str_iterable(1243421) == True
    assert palindrome_str_iterable(2) == True
    assert palindrome_str_iterable(0) == True
    assert palindrome_str_iterable(11) == True
    assert palindrome_str_iterable("") == "Valor necessário"
    assert palindrome_str_iterable("123") == "Valor numerico necessário"
    assert palindrome_str_iterable(123.12) == "Valor numerico necessário"
    assert palindrome_str_iterable([1, 2, 3]) == "Valor numerico necessário"
    assert palindrome_str_iterable(112) == False
    assert palindrome_str_iterable(123456) == False
    assert palindrome_str_iterable(11111112) == False
    assert palindrome_str_iterable(111111111111111111112) == False

def test_palindrome_without_str():
    assert palindrome_without_str(12321) == True
    assert palindrome_without_str(1243421) == True
    assert palindrome_without_str(2) == True
    assert palindrome_without_str(0) == True
    assert palindrome_without_str(11) == True
    assert palindrome_without_str("") == "Valor necessário"
    assert palindrome_without_str("123") == "Valor numerico necessário"
    assert palindrome_without_str(123.12) == "Valor numerico necessário"
    assert palindrome_without_str([1, 2, 3]) == "Valor numerico necessário"
    assert palindrome_without_str(112) == False
    assert palindrome_without_str(123456) == False
    assert palindrome_without_str(11111112) == False
    assert palindrome_without_str(111111111111111111112) == False

retcode = pytest.main()