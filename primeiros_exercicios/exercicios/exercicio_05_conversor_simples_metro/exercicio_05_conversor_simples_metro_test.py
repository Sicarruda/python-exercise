from primeiros_exercicios.exercicios.exercicio_05_conversor_simples_metro.exercicio_05_conversor_simples_metro import conversor

def test_verifica_se_metros_sao_convertidos_para_centimetros():
    metros = 10
    centimetros = metros * 100
    assert conversor(metros) == f'{metros}, metros equivale a {centimetros} centimetros'
