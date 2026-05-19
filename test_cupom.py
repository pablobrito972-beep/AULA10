from cupom import aplicar_cupom

def test_cupom10_deve_retornar_10_porcento():
    assert aplicar_cupom("CUPOM10", 50.0) == 0.10

def test_cupom10_minusculo_deve_funcionar():
    # Testa que maiúsculas e minúsculas são tratadas igual
    assert aplicar_cupom("cupom10", 50.0) == 0.10

def test_cupom25_com_valor_acima_de_100_deve_retornar_25_porcento():
    assert aplicar_cupom("CUPOM25", 150.0) == 0.25

def test_cupom25_com_valor_abaixo_de_100_deve_retornar_zero():
    assert aplicar_cupom("CUPOM25", 50.0) == 0.0

def test_descontovip_com_valor_acima_de_500_deve_retornar_35_porcento():
    assert aplicar_cupom("DESCONTOVIP", 600.0) == 0.35

def test_descontovip_com_valor_abaixo_de_500_deve_retornar_zero():
    assert aplicar_cupom("DESCONTOVIP", 300.0) == 0.0

def test_cupom_invalido_deve_retornar_zero():
    assert aplicar_cupom("CUPOM_FALSO", 200.0) == 0.0