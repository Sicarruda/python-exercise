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
	balde_18_litros = 108 
	balde_3_6_litros = 21.6 
	baldes_menor_custo = {
		"balde_18_litros":0, 
		"balde_3_6_litros":0,
		"valor_balde_18_litros": 80,
		"valor_balde_3_6_litros": 25,
		}
	qnt_baldes_18_litros = area / balde_18_litros
	qnt_baldes_3_6_litros = area / balde_3_6_litros
	area_mais_10 = area * 1.1
	area_regresiva = area_mais_10
	while area_mais_10 > 0:
		if area_regresiva <= 64.8:
			baldes_menor_custo["balde_3_6_litros"] = math.ceil(area_regresiva / balde_3_6_litros)
			area_mais_10 = 0

		area_regresiva = area_regresiva - balde_18_litros

		if area_regresiva >= 0:
			baldes_menor_custo["balde_18_litros"] = baldes_menor_custo["balde_18_litros"] + 1

	print(f"comprar apenas latas de 18 litros R${math.ceil(qnt_baldes_18_litros) * baldes_menor_custo['valor_balde_18_litros']}")
	print(f"comprar apenas latas de 3,6 litros R${math.ceil(qnt_baldes_3_6_litros) * baldes_menor_custo['valor_balde_3_6_litros']}")
	print(f"Mistura de galões pelo menor preço: latas 18 litros {baldes_menor_custo['balde_18_litros']}, latas 3,6 litros {baldes_menor_custo['balde_3_6_litros']} totalizando R${(baldes_menor_custo['babalde_18_litroslde_18'] * baldes_menor_custo['valor_balde_18_litros']) + (baldes_menor_custo['babalde_3_6_litroslde_3'] * baldes_menor_custo['valor_balde_3_6_litros']) }")

calculadora_tinta(metros_quadrados)
