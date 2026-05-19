PRECO_INTEIRA = 40
PRECO_MEIA = PRECO_INTEIRA // 2
PRECO_ISENTO = 0

def definir_preco_ingresso(idade):
    if idade < 4:
        return 0
    elif idade <= 18 or idade >= 60:
        return 20
    return 40
    