import pytest
from exercicio_03_funcao_simples import soma_2_num

def test_verifica_se_soma_correta():
    soma_int = [1, 1, 2]
    soma_int_gande = [50000000, 321654987, 371654987 ]
    soma_a_errado = ["erado", 5, 0]
    soma_b_errado = [5, 'errado', 0]
    soma_negativo = [-5,-10,-15]
    soma_a_negativo = [-5, 5, 0]
    soma_b_negativo = [5, -5, 0]

    assert soma_2_num(soma_int[0], soma_int[1]) == f'a soma de {soma_int[0]} mais {soma_int[1]} é {soma_int[2]}'
    assert soma_2_num(soma_int_gande[0], soma_int_gande[1]) == f'a soma de {soma_int_gande[0]} mais {soma_int_gande[1]} é {soma_int_gande[2]}'
    assert soma_2_num(soma_negativo[0], soma_negativo[1]) == f'a soma de {soma_negativo[0]} mais {soma_negativo[1]} é {soma_negativo[2]}'
    assert soma_2_num(soma_a_negativo[0],soma_a_negativo[1]) == f'a soma de {soma_a_negativo[0]} mais {soma_a_negativo[1]} é {soma_a_negativo[2]}'
    assert soma_2_num(soma_b_negativo[0],soma_b_negativo[1]) == f'a soma de {soma_b_negativo[0]} mais {soma_b_negativo[1]} é {soma_b_negativo[2]}'
    
    with pytest.raises(TypeError) as error:
        soma_2_num(soma_a_errado[0],soma_a_errado[1])
    assert "can only concatenate str" in str(error.value)
    
    with pytest.raises(TypeError) as error:
        soma_2_num(soma_b_errado[0],soma_b_errado[1])
    assert "unsupported operand type(s) for +: 'int' and 'str'" in str(error.value)
    

