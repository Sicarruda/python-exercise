'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'''


def calcula_area_circulo(raio):
    area_circulo = 3.14*(raio**2)
    return f'A area do circulo é {area_circulo}'
    

if __name__ == '__main__':
    raio = int(input('Digite o raio '))
    calcula_area_circulo(raio)
