from unittest.mock import patch
from Exercicio4 import criar_identificacao

def test_mensagem_gerada_corretamente():
    with patch("Exercicio4.gerar_codigo") as mock_gerar_codigo:
        mock_gerar_codigo.return_value = "USR-1234"
        msg = criar_identificacao("Carlos")
        assert msg == "Usuário Carlos cadastrado com código USR-1234."

def test_gerar_codigo_foi_chamada():
    with patch("Exercicio4.gerar_codigo") as mock_gerar_codigo:
        mock_gerar_codigo.return_value = "USR-1234"
        criar_identificacao("Carlos")
        mock_gerar_codigo.assert_called()

def test_gerar_codigo_chamada_apenas_uma_vez():
    with patch("Exercicio4.gerar_codigo") as mock_gerar_codigo:
        mock_gerar_codigo.return_value = "USR-1234"
        criar_identificacao("Carlos")
        mock_gerar_codigo.assert_called_once_with()

def test_mock_codigo_0001():
    with patch("Exercicio4.gerar_codigo") as mock_gerar_codigo:
        mock_gerar_codigo.return_value = "USR-0001"
        msg = criar_identificacao("Carlos")
        assert msg == "Usuário Carlos cadastrado com código USR-0001."

def test_mock_codigo_9999():
    with patch("Exercicio4.gerar_codigo") as mock_gerar_codigo:
        mock_gerar_codigo.return_value = "USR-9999"
        msg = criar_identificacao("Carlos")
        assert msg == "Usuário Carlos cadastrado com código USR-9999."

def test_nomes_diferentes():
    with patch("Exercicio4.gerar_codigo") as mock_gerar_codigo:
        mock_gerar_codigo.return_value = "USR-1234"
        msg_ana = criar_identificacao("Ana")
        msg_joao = criar_identificacao("João")
        assert msg_ana == "Usuário Ana cadastrado com código USR-1234."
        assert msg_joao == "Usuário João cadastrado com código USR-1234."
