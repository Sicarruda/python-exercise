import pytest
from exercicios.exercicio_02_input_simples import formata_mensagem_usuario

def test_exibe_mensagem_do_ususario_correta():
    assert formata_mensagem_usuario(5) == 'O numero informado foi 5'
    assert formata_mensagem_usuario(6) == 'O numero informado foi 6'
    assert formata_mensagem_usuario(-6) == 'O numero informado foi -6'
    assert formata_mensagem_usuario(50000000000) == 'O numero informado foi 50000000000'

    with pytest.raises(TypeError) as error:
        formata_mensagem_usuario()
    assert "missing 1 required positional argument: 'valor'" in str(error.value)

    with pytest.raises(TypeError) as error:
        formata_mensagem_usuario("GABRIEL")
    assert "Valor não permitido" in str(error.value)
   