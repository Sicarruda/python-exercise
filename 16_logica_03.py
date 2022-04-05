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

PREENCHIMENTO_POR_LITRO = 6
COBERTURA_BALDE_18_000_MILILITROS = 18 * PREENCHIMENTO_POR_LITRO
COBERTURA_BALDE_3_600_MILILITROS = 3.6 * PREENCHIMENTO_POR_LITRO
VALOR_BALDE_18_000_MILILITROS = 80
VALOR_BALDE_3_600_MILILITROS = 25
MENOR_AREA_DE_CUSTO = int(VALOR_BALDE_18_000_MILILITROS / VALOR_BALDE_3_600_MILILITROS) * COBERTURA_BALDE_3_600_MILILITROS


def calculadora_tinta(area):
	
	baldes_menor_custo = {
		"balde_18_litros":0, 
		"balde_3_6_litros":0,
		}

	qnt_baldes_18_litros = area / COBERTURA_BALDE_18_000_MILILITROS
	qnt_baldes_3_6_litros = area / COBERTURA_BALDE_3_600_MILILITROS
	area_com_margem_segurança = area * 1.1
	area_restante = area_com_margem_segurança
	while area_com_margem_segurança > 0:
		if area_restante <= MENOR_AREA_DE_CUSTO:
			baldes_menor_custo["balde_3_6_litros"] = math.ceil(area_restante / COBERTURA_BALDE_3_600_MILILITROS)
			area_com_margem_segurança = 0

		area_restante = area_restante - COBERTURA_BALDE_18_000_MILILITROS

		if area_restante >= 0:
			baldes_menor_custo["balde_18_litros"] = baldes_menor_custo["balde_18_litros"] + 1

	print(f"comprar apenas latas de 18 litros R${ math.ceil(qnt_baldes_18_litros) * VALOR_BALDE_18_000_MILILITROS }")
	print(f"comprar apenas latas de 3,6 litros R${ math.ceil(qnt_baldes_3_6_litros) * VALOR_BALDE_3_600_MILILITROS }")
	print(f"Mistura de galões pelo menor preço: latas 18 litros { baldes_menor_custo['balde_18_litros'] }, latas 3,6 litros {baldes_menor_custo['balde_3_6_litros'] } totalizando R$ { (baldes_menor_custo['balde_18_litros'] * VALOR_BALDE_18_000_MILILITROS) + (baldes_menor_custo['balde_3_6_litroslde_3'] * VALOR_BALDE_3_600_MILILITROS) }")


metros_quadrados = float(input('Digite o numero em m² da area: '))

calculadora_tinta(metros_quadrados)
