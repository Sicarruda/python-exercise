
'''Faça um Programa que peça a temperatura em graus Farenheit, transforme e
mostre a temperatura em graus Celsius.
    C = (5 * (F-32) / 9). '''

def conversor_celcius():
    Farenheit = int(input('Digite a temperatura em Farenheit '))
    Celcius = (5 * (Farenheit-32) / 9)
    print ('A temperatura em Celcius é de ', Celcius)


'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre
em graus Farenheit. '''

def conversor_farenheit():
    Celcius = int(input('Digite a temperatura em Celcius '))
    Farenheit = (Celcius * 9/5) + 32 
    print ('A temperatura em Farenheit é de ', Farenheit)