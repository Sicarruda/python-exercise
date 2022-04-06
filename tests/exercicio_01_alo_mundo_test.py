from exercicios.exercicio_01_alo_mundo import print_mensagem


def test_verifica_se_imput_esta_correto():
    assert print_mensagem() == 'Alo mundo!'

