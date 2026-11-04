def classificar_produto(quantidade):
    if quantidade == 0:
        return "Sem estoque"
    if 1 <= quantidade <= 5:
        return "Estoque baixo"
    if 6 <= quantidade <= 20:
        return "Estoque normal"
    if quantidade > 20:
        return "Estoque alto"
    if quantidade < 0:
        return "Quantidade inválida"