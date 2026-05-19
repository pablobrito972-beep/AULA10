from notas import converter_nota_para_conceito

def test_nota_invalida_abaixo_de_zero():
    assert converter_nota_para_conceito(-1) == "Nota inválida"

def test_nota_invalida_acima_de_10():
    assert converter_nota_para_conceito(11) == "Nota inválida"

def test_nota_conceito_A():
    assert converter_nota_para_conceito(10.0) == "A"
    assert converter_nota_para_conceito(9.0)  == "A"  # caso limite

def test_nota_conceito_B():
    assert converter_nota_para_conceito(8.9) == "B"   # caso limite
    assert converter_nota_para_conceito(7.0) == "B"   # caso limite

def test_nota_conceito_C():
    assert converter_nota_para_conceito(6.9) == "C"   # caso limite
    assert converter_nota_para_conceito(5.0) == "C"   # caso limite

def test_nota_conceito_D():
    assert converter_nota_para_conceito(4.9) == "D"   # caso limite
    assert converter_nota_para_conceito(3.0) == "D"   # caso limite

def test_nota_conceito_F():
    assert converter_nota_para_conceito(2.9) == "F"   # caso limite
    assert converter_nota_para_conceito(0.0) == "F"