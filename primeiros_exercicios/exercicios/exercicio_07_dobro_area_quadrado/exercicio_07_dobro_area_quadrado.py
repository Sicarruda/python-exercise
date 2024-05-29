'''Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro
desta área para o usuário.'''

lado_quadrado = int(input('digite o tamanho de um dos lados do quadrado '))

def dobro_area_quadrado(lado_quadrado):
    area_quadrado_dobrada = (lado_quadrado**2)*2
    print ('O dobro da area do quadrado é ',area_quadrado_dobrada)
