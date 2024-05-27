import pytest

from devolve_troco import *

def test_retorna_troco():
    assert devolve_troco(0, 0) == "Valor de pagamento insuficiente"
    assert devolve_troco(23, 0) == "Valor de compra insuficiente"
    assert devolve_troco(50, 20) == {"20": 1, "10": 1}
    assert devolve_troco(32.25, 21.10) == {"10": 1, "1": 1, "0.1": 1, "0.05": 1}
    assert devolve_troco(50, 48.34) == {
        "1": 1,
        "0.5": 1,
        "0.1": 1,
        "0.05": 1,
        "0.01": 1,
    }
    assert devolve_troco(9.12, 10) == "Valor de pagamento insuficiente"
    assert devolve_troco("1", 5) == "Somente valores numéricos"
    assert devolve_troco("2", "0,25") == "Somente valores numéricos"
    assert devolve_troco([52],12) == "Somente valores numéricos"
    assert devolve_troco({"valor": 123}, [123]) == "Somente valores numéricos"


retcode = pytest.main()
