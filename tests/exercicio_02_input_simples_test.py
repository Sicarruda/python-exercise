from exercicios.exercicio_02_input_simples import print_mensagem_usuario

def test_exibe_mensagem_do_ususario_correta():
    assert print_mensagem_usuario(5) == 'O numero informado foi 5'
