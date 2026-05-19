from bonus import calcular_bonus

def test_avaliacao_bom_deve_retornar_10_porcento():
    assert calcular_bonus(1000.0, "Bom") == 100.0

def test_avaliacao_excelente_deve_retornar_20_porcento():
    assert calcular_bonus(1000.0, "Excelente") == 200.0

def test_avaliacao_regular_deve_retornar_2_porcento():
    assert calcular_bonus(1000.0, "Regular") == 20.0

def test_avaliacao_ruim_deve_retornar_zero():
    assert calcular_bonus(1000.0, "Ruim") == 0.0

def test_avaliacao_invalida_deve_retornar_zero():
    assert calcular_bonus(1000.0, "Mais ou Menos") == 0.0

def test_salario_negativo_deve_retornar_zero():
    assert calcular_bonus(-500.0, "Excelente") == 0.0