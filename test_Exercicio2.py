from Exercicio2 import inverter_palavras

def test_frase_varias_palavras():
    palavra = inverter_palavras("Python é muito interessante")
    assert palavra == "interessante muito é Python"

def test_frase_apenas_1_palavra():
    palavra = inverter_palavras("Python")
    assert palavra == "Python"

def test_frase_vazia():
    palavra = inverter_palavras("")
    assert palavra == ""

def test_frase_espaco_extra():
    palavra = inverter_palavras("Python  é muito   interessante")
    assert palavra == "interessante muito é Python"

def test_frase_numero_letra():
    palavra = inverter_palavras("Python 1 é muito 2 interessante 3")
    assert palavra == "3 interessante 2 muito é 1 Python"