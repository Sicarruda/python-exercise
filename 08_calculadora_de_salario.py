'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''

salario_hora = int(input('Digite quanto você ganha por hora '))
hora_trabalho = int(input('Digite quantas horas você trabalha por dia '))


def calculadora_salario(salario_hora, hora_trabalho):
    total_salario = (salario_hora * hora_trabalho) * (5 * 4)
    print ('Você ganha um total de ',total_salario,' por mês')
