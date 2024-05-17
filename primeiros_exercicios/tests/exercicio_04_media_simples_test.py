from primeiros_exercicios.exercicios.exercicio_04_media_simples import media_notas

def test_verifica_media_de_notas():
    n1 = 1
    n2 = 1
    n3 = 1
    n4 = 1
    media = (n1 + n2 + n3 + n4) / 4
    assert media_notas(n1,n2,n3,n4) == f'Sua média é {media}'