def aplicar_cupom(codigo_cupom, valor_compra):
    # Deixa o código todo em minúsculo para não diferenciar maiúsculas de minúsculas
    codigo = codigo_cupom.lower()

    if codigo == "cupom10":
        return 0.10
    elif codigo == "cupom25":
        if valor_compra > 100.0:
            return 0.25
        else:
            return 0.0
    elif codigo == "descontovip":
        if valor_compra > 500.0:
            return 0.35
        else:
            return 0.0
    else:
        return 0.0