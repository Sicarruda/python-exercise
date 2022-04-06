from exercicios.exercicio_03_funcao_simples import input_2_num

def test_verifica_se_soma_correta():
    a = 2
    b = 3
    c = 5
    assert input_2_num(a, b) == f'a soma de {a} mais {b} é {c}'