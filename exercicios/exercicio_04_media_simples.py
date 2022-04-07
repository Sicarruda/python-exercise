'''Faça um Programa que peça as 4 notas bimestrais e mostre a média.'''


def media_notas(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    return f'Sua média é {media}'


if __name__ == "__main__":
    print ('Olá, vamos saber qual a sua média deste ano? Primeiro me diga quais as suas 4 notas bimestrais')
    nota1 = int(input('Primeira nota: '))
    nota2 = int(input('Segunda nota: '))
    nota3 = int(input('Terceira nota: '))
    nota4 = int(input('Quarta nota: '))

    media_notas(nota1, nota2, nota3, nota4)