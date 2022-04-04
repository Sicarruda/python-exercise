import math

'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de
1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
    preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o preço seja o menor. Acrescente 10%
    de folga e sempre arredonde os valores para cima, isto é, considere latas
    cheias. '''

metros_quadrados = float(input('Digite o numero em m² da area: '))

def calculadora_tinta(area):
	balde_18 = 108 
	balde_3 = 21.6 # balde tem 3,6 litros na vdd
	baldes_menor_custo = {
		"balde_18":0, 
		"balde_3":0,
		"valor_18": 80,
		"valor_3": 25,
		}
	qnt_baldes_18 = area / balde_18
	qnt_baldes_3 = area / balde_3
	count_area = area * 1.1
	count = count_area
	while count_area > 0:
		if count <= 64.8:
			baldes_menor_custo["balde_3"] = math.ceil(count / balde_3)
			count_area = 0
		count = count - balde_18
		if count > 0:
			baldes_menor_custo["balde_18"] = baldes_menor_custo["balde_18"] + 1

	print(f"comprar apenas latas de 18 litros R${math.ceil(qnt_baldes_18) * baldes_menor_custo['valor_18']}")
	print(f"comprar apenas latas de 3,6 litros R${math.ceil(qnt_baldes_3) * baldes_menor_custo['valor_3']}")
	print(f"Mistura de galões pelo menor preço: latas 18 litros {baldes_menor_custo['balde_18']}, latas 3,6 litros {baldes_menor_custo['balde_3']} totalizando R${(baldes_menor_custo['balde_18'] * baldes_menor_custo['valor_18']) + (baldes_menor_custo['balde_3'] * baldes_menor_custo['valor_3']) }")

calculadora_tinta(metros_quadrados)
