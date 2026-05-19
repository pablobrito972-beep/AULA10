from bilheteria import definir_preco_ingresso, PRECO_INTEIRA, PRECO_ISENTO, PRECO_MEIA

def test_ingresso_isento():
    assert definir_preco_ingresso(1) == 0
    assert definir_preco_ingresso(2) == 0
    assert definir_preco_ingresso(3) == 0
    
def test_ingresso_jovem():
    for i in range(4, 19):
        assert definir_preco_ingresso(i) == 20
        
def test_ingresso_adulto():
    for i in range(19, 60):
        assert definir_preco_ingresso(i) == 40
        
def test_ingresso_idoso():
    assert definir_preco_ingresso(60) == 20
    assert definir_preco_ingresso(75) == 20
    assert definir_preco_ingresso(94) == 20