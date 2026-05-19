from frete import calcular_frete

def test_peso_zero_deve_retornar_frete_zero():
    assert calcular_frete(0) == 0.0

def test_peso_negativo_deve_retornar_frete_zero():
    assert calcular_frete(-10) == 0.0

def test_peso_ate_1kg_deve_retornar_5_reais():
    assert calcular_frete(0.5) == 5.0
    assert calcular_frete(1.0) == 5.0   # caso limite

def test_peso_acima_1kg_ate_5kg_deve_retornar_10_reais():
    assert calcular_frete(1.01) == 10.0  # caso limite
    assert calcular_frete(3.0)  == 10.0
    assert calcular_frete(5.0)  == 10.0  # caso limite

def test_peso_acima_5kg_deve_retornar_18_reais():
    assert calcular_frete(5.01) == 18.0  # caso limite
    assert calcular_frete(10.0) == 18.0