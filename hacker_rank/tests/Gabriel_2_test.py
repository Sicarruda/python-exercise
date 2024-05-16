from execicios.Gabriel_2 import *

valores_testes = [(0, 0), (50, 20), (32.25, 21.10), (50, 48.34), (9.12, 10),("1",5),("2","0,25")]
respostas_trocos = [
    {},
    {"20": 1, "10": 1},
    {"10": 1, "1": 1, "0.1": 1, "0.05": 1},
    {"1": 1, "0.5": 1, "0.1": 1, "0.05": 1, "0.01": 1},
    "Valor de pagamento insuficiente",
    "Somente valores numéricos",
    "Somente valores numéricos"
]


def test_retorna_troco():
    for item in range(len(valores_testes)):
        assert devolve_troco(valores_testes[item][0],valores_testes[item][1]) == respostas_trocos[item]

