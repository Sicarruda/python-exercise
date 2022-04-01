'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'''

raio = int(input('Digite o raio '))

def area_circulo(raio):
    area_circulo = 3.14*(raio**2)
    print ('A area do circulo é ',area_circulo)
    