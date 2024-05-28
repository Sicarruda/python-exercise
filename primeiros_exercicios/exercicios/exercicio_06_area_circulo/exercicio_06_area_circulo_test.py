from primeiros_exercicios.exercicios.exercicio_06_area_circulo.exercicio_06_area_circulo import calcula_area_circulo

def test_verifica_area_de_um_circulo():
    raio = 5
    area_circulo = 78.5
    assert calcula_area_circulo(raio) == f'A area do circulo é {area_circulo}'