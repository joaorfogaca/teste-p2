from unittest.mock import patch
from Exercicio5 import acessar_sistema

def test_usuario_com_permissao():
    with patch("Exercicio5.verificar_permissao") as mock_verificar_permissao:
        mock_verificar_permissao.return_value = True
        retorno = acessar_sistema("Carlos")
        assert retorno == "Acesso autorizado"

def test_usuario_sem_permissao():
    with patch("Exercicio5.verificar_permissao") as mock_verificar_permissao:
        mock_verificar_permissao.return_value = False
        retorno = acessar_sistema("Pedro")
        assert retorno == "Acesso negado"

def test_verificar_permissao_foi_chamada():
    with patch("Exercicio5.verificar_permissao") as mock_verificar_permissao:
        mock_verificar_permissao.return_value = True
        acessar_sistema("Carlos")
        mock_verificar_permissao.assert_called_once()

def test_verificar_permissao_chamada_com_usuario_correto():
    with patch("Exercicio5.verificar_permissao") as mock_verificar_permissao:
        mock_verificar_permissao.return_value = True
        acessar_sistema("Carlos")
        mock_verificar_permissao.assert_called_once_with("Carlos")

def test_mock_simula_os_dois_cenarios():
    with patch("Exercicio5.verificar_permissao") as mock_verificar_permissao:
        mock_verificar_permissao.side_effect = [True, False]
        autorizado = acessar_sistema("Carlos")
        negado = acessar_sistema("Pedro")
        assert autorizado == "Acesso autorizado"
        assert negado == "Acesso negado"
