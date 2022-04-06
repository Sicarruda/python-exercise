'''Faça um Programa que converta metros para centímetros.'''

def conversor(metros):
	centimetros = metros * 100
	return f'{metros}, metros equivale a {centimetros} centimetros'


if __name__ == '__main__':
	metros = int(input('insira a metragem: '))

	