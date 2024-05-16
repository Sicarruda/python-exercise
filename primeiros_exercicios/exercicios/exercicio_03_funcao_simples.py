'''Faça um Programa que peça dois números e imprima a soma.'''

def soma_2_num(a, b):
	if type(a) != int and type(b) != int:
		raise TypeError("Valores incorretos")
	c = a + b
	return f'a soma de {a} mais {b} é {c}'
	
    
if __name__ == '__main__':
    a = int(input('Digite um numero numero '))
    b = int(input('Digite outro numero numero '))
    soma_2_num(a,b)