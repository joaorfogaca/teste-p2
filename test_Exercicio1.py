from Exercicio1 import classificar_produto

def test_produto_sem_estoque():
    qtd = 0
    retorno = classificar_produto(qtd)
    assert retorno == "Sem estoque"

def test_produto_com_estoque_baixo():
    qtd = 3
    retorno = classificar_produto(qtd)
    assert retorno == "Estoque baixo"

def test_produto_com_estoque_normal():
    qtd = 8
    retorno = classificar_produto(qtd)
    assert retorno == "Estoque normal"

def test_produto_com_estoque_alto():
    qtd = 30
    retorno = classificar_produto(qtd)
    assert retorno == "Estoque alto"

def test_produto_com_estoque_negativo():
    qtd = -30
    retorno = classificar_produto(qtd)
    assert retorno == "Quantidade inválida"
