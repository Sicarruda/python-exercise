#Atividades de estudo

'''Faça um Programa que mostre a mensagem "Alo mundo" na tela.'''
   
A = ' Alo mundo!'
print (A)

'''Faça um Programa que peça um número e então mostre a mensagem O número
informado foi [número].'''

B = int(input('Digite um numero '))
print ( 'o numero informado foi ', B)

'''Faça um Programa que peça dois números e imprima a soma.'''

D = int(input('Digite outro numero numero '))
E = B + D
print ('a soma de ',B,' mais ',D,' é ',E)

'''Faça um Programa que peça as 4 notas bimestrais e mostre a média.'''

print ('Olá, vamos saber qual a sua média deste ano? Primeiro me diga quais as suas 4 notas bimestrais')
nota1 = int(input('Primeira nota: '))
nota2 = int(input('Segunda nota: '))
nota3 = int(input('Terceira nota: '))
nota4 = int(input('Quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print ('Sua média é ', media)
   
'''Faça um Programa que converta metros para centímetros.'''

metros = int(input('insira a metragem: '))
centimetros = metros * 100
print (metros, 'metros equivale a', centimetros, 'centimetros')

'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'''

raio = int(input('Digite o raio '))
area_circulo = 3.14*(raio**2)
print ('A area do circulo é ',area_circulo)

'''Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro
desta área para o usuário.'''

lado_quadrado = int(input('digite o tamanho de um dos lados do quadrado '))
area_quadrado = (lado_quadrado**2)*2
print ('O dobro da area do quadrado é ',area_quadrado)

'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''

salario_hora = int(input('Digite quanto você ganha por hora '))
hora_trabalho = int(input('Digite quantas horas você trabalha por dia '))
total_salario = (salario_hora*hora_trabalho)*(5*4)
print ('Você ganha um total de ',total_salario,' por mês')

'''Faça um Programa que peça a temperatura em graus Farenheit, transforme e
mostre a temperatura em graus Celsius.
    C = (5 * (F-32) / 9). '''

Farenheit = int(input('Digite a temperatura em Farenheit '))
Celcius = (5 * (Farenheit-32) / 9)
print ('A temperatura em Celcius é de ', Celcius)
                         
'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre
em graus Farenheit. '''

Celcius2 = int(input('Digite a temperatura em Celcius '))
Farenheit2 = (Celcius2 * 9/5) + 32 
print ('A temperatura em Farenheit é de ', Farenheit2)

'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e
mostre:
   a)o produto do dobro do primeiro com metade do segundo .
   b)a soma do triplo do primeiro com o terceiro.
   c)o terceiro elevado ao cubo. '''

num1 = int(input('Digite um numero inteiro '))
num2 = int(input('Digite outro numero inteiro '))
num3 = float(input('Digite um numero real '))
conta1 = (num1 * 2) * (num2 / 2)
conta2 = num1 * 3 + num3
conta3 = num3 ** 3
print ('o produto do dobro do primeiro com metade do segundo é ',conta1)
print ('a soma do triplo do primeiro com o terceiro é ',conta2)
print (' o terceiro elevado ao cubo é ',conta3)

'''Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58'''

'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
que calcule seu peso ideal, utilizando as seguintes fórmulas:

    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7 '''

'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes
maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que
você faça um programa que leia a variável peso (peso de peixes) e calcule o
excesso. Gravar na variável excesso a quantidade de quilos além do limite e na
variável multa o valor da multa que João deverá pagar. Imprima os dados do
programa com as mensagens adequadas. '''

'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
para o sindicato, faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

    Obs.: Salário Bruto - Descontos = Salário Líquido.'''

'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1
litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total. '''

'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de
1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
    preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o preço seja o menor. Acrescente 10%
    de folga e sempre arredonde os valores para cima, isto é, considere latas
    cheias. '''

'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado
de download do arquivo usando este link (em minutos). '''

    
