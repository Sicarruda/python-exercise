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


def calculadora_tinta_balde_18_000_litros(area):
    qnt_baldes_18_litros = math.ceil(area / COBERTURA_BALDE_18_000_MILILITROS)
    valor_total = qnt_baldes_18_litros * VALOR_BALDE_18_000_MILILITROS
    valor_e_qnts = [valor_total, qnt_baldes_18_litros]
    return valor_e_qnts


def calculadora_tinta_balde_3_600_litros(area):
    qnt_baldes_3_6_litros = math.ceil(area / COBERTURA_BALDE_3_600_MILILITROS)
    valor_total = round(qnt_baldes_3_6_litros * VALOR_BALDE_3_600_MILILITROS, 2)
    valor_e_qnts = [valor_total, qnt_baldes_3_6_litros]
    return valor_e_qnts


def calculadora_tinta_mix(area):
    balde_3_6_litros = 0
    balde_18_litros = 0	
    area_com_margem_segurança = area * 1.1
    area_restante = area_com_margem_segurança

    while area_com_margem_segurança > 0:
        if area_restante <= MENOR_AREA_DE_CUSTO:
            balde_3_6_litros = round(math.ceil(area_restante / COBERTURA_BALDE_3_600_MILILITROS),2)
            area_com_margem_segurança = -1

        area_restante = area_restante - COBERTURA_BALDE_18_000_MILILITROS

        if area_restante >= 0:
            balde_18_litros = balde_18_litros + 1
    
    valor_total_18 = round(balde_18_litros * VALOR_BALDE_18_000_MILILITROS, 2)
    valor_total_3_6 = round(balde_3_6_litros * VALOR_BALDE_3_600_MILILITROS, 2)
    valor_e_qnts = [valor_total_18, balde_18_litros, valor_total_3_6, balde_3_6_litros ]
    return valor_e_qnts


def exibe_valores_qnts(array_18l, array_3_6l, array_mix):
    exibicao_18l = f"comprando apenas latas de 18 litros serão {array_18l[1]} latas, total de R${array_18l[0]}"
    exibicao_3_6l = f"comprando apenas latas de 3,6 litros serão {array_3_6l[1]} latas, total de R${array_3_6l[0]}"
    exibicao_mix = f"comprando apenas latas mistas serão {array_mix[1]} latas de 18 litros, custando R${array_mix[0]} e {array_mix[3]} latas de 3,6 litros, custando R${array_mix[2]}.Total de R${array_mix[0] + array_mix[2]} "
    print(exibicao_18l)
    print(exibicao_3_6l)
    print(exibicao_mix)


metros_quadrados = float(input('Digite o numero em m² da area: '))

exibe_valores_qnts(calculadora_tinta_balde_18_000_litros(metros_quadrados), calculadora_tinta_balde_3_600_litros(metros_quadrados),calculadora_tinta_mix(metros_quadrados))


