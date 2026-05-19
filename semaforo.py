def acao_semaforo(cor):
    if cor == "vermelho":
        return "Pare"
    elif cor == "amarelo":
        return "Atenção"
    elif cor == "verde":
        return "Siga"
    else:
        return "Cor inválida"