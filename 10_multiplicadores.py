'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e
mostre:
   a)o produto do dobro do primeiro com metade do segundo . conta1
   b)a soma do triplo do primeiro com o terceiro. conta2
   c)o terceiro elevado ao cubo. conta3 '''

num1 = int(input('Digite um numero inteiro '))
num2 = int(input('Digite outro numero inteiro '))
num_real = float(input('Digite um numero real '))
conta1 = (num1 * 2) * (num2 / 2)
conta2 = num1 * 3 + num_real
conta3 = num_real ** 3
print ('o produto do dobro do primeiro com metade do segundo é ',conta1)
print ('a soma do triplo do primeiro com o terceiro é ',conta2)
print (' o terceiro elevado ao cubo é ',conta3)