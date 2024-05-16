"""
    De o troco usando moedas e notas. Ex: entrada 50 valor: 32,51 como devolver o troco?
"""

def devolve_troco(pagamento,compra):
    try:
        if pagamento < compra:
            raise ValueError("Valor de pagamento insuficiente")

        troco = round(pagamento - compra, 2)
        total_troco = {}
        notas_moedas_disponiveis = {
            "100": 0,
            "50": 0,
            "20": 0,
            "10": 0,
            "5": 0,
            "2": 0,
            "1": 0,
            "0.5": 0,
            "0.25": 0,
            "0.1": 0,
            "0.05": 0,
            "0.01": 0
        }

        notas_moedas_para_troco = [float(key) for key in notas_moedas_disponiveis.keys()]

        while troco > 0:
            for nota_moeda in notas_moedas_para_troco:
                if nota_moeda <= troco:
                    troco = round(troco - nota_moeda, 2)

                    if int(nota_moeda) > 0:
                        notas_moedas_disponiveis[str(int(nota_moeda))] += 1

                    else:
                        notas_moedas_disponiveis[str(nota_moeda)] += 1

                    break
                
        for nota_moeda in notas_moedas_disponiveis.keys():
            if notas_moedas_disponiveis[nota_moeda] >= 1:
                total_troco[nota_moeda] = notas_moedas_disponiveis[nota_moeda]

        return total_troco

    except ValueError as e:
        return str(e)
    except TypeError:
        return "Somente valores numéricos"

print(devolve_troco("9.12",10))

