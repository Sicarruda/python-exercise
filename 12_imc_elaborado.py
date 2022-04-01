'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
que calcule seu peso ideal, utilizando as seguintes fórmulas:

    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7 '''

def imc():
    altura = float(input('Digite sua altura: '))
    sexo = str(input('Digite f para feminino e m para masculino: '))
    if sexo == "f":
        conta_imc_f = (62.1 * altura) - 44.7
        print(f'Seu imc é ${conta_imc_f}')
    elif sexo == "m":
        conta_imc_m = (72.7 * altura) - 58
        print(f'Seu imc é ${conta_imc_m}')
    else:
        print(f'Informação sobre sexo incorreta, tente de novo')

