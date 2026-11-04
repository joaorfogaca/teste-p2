from Exercicio3 import validar_documento

def test_documento_com_11_digitos():
    documento = "12345678900"
    retorno = validar_documento(documento)
    assert retorno is True

def test_documento_formatado():
    documento = "123.456.789-00"
    retorno = validar_documento(documento)
    assert retorno is True

def test_documento_com_menos_de_11_digitos():
    documento = "123456789"
    retorno = validar_documento(documento)
    assert retorno is False

def test_documento_com_mais_de_11_digitos():
    documento = "123456789001"
    retorno = validar_documento(documento)
    assert retorno is False

def test_documento_com_letras():
    documento = "1234567890a"
    retorno = validar_documento(documento)
    assert retorno is False

def test_documento_vazio():
    documento = ""
    retorno = validar_documento(documento)
    assert retorno is False
