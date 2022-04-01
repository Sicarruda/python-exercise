'''Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58'''

def imc():
    altura = float(input('Digite sua altura: '))
    conta_imc = (72.7*altura) - 58
    print(f'Seu imc é ${conta_imc}')

