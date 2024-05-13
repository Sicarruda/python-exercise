"""
    De o troco usando moedas e notas. Ex: entrada 50 valor: 32,51 como devolver o troco?
"""

def devolve_troco(valor,pag):

    if valor > pag:

        subt = round(valor - pag, 2)
        notas_moedas = {
            "100":0,
            "50":0,
            "20":0,
            "10":0,
            "5":0,
            "2":0,
            "1":0,
            "0.5":0,
            "0.25":0,
            "0.1":0,
            "0.05":0,
            "0.01":0
        }

        keys_int = [float(key) for key in notas_moedas.keys()]

        while subt > 0:

            for i in keys_int:

                if i <= subt:
                    subt = round(subt - i, 2)

                    if int(i) > 0: 
                        notas_moedas[str(int(i))] += 1 
                    else:
                        notas_moedas[str(i)] += 1
                    
                    break

        return notas_moedas
    
    else:
        msg = "Valor de pagamento insuficiente"

        return msg


print(devolve_troco(299,278))

