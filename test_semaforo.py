from semaforo import acao_semaforo

def test_cor_vermelho_deve_retornar_pare():
    assert acao_semaforo("vermelho") == "Pare"

def test_cor_amarelo_deve_retornar_atencao():
    assert acao_semaforo("amarelo") == "Atenção"

def test_cor_verde_deve_retornar_siga():
    assert acao_semaforo("verde") == "Siga"

def test_cor_invalida_deve_retornar_mensagem():
    assert acao_semaforo("azul") == "Cor inválida"
    assert acao_semaforo("roxo") == "Cor inválida"
    