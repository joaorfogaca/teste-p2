from unittest.mock import patch
from Exercicio6 import atender_proximo_cliente

def test_atendimento_realizado_com_sucesso():
    with patch("Exercicio6.obter_proximo_cliente") as mock_obter_cliente:
        with patch("Exercicio6.registrar_atendimento") as mock_registrar:
            mock_obter_cliente.return_value = "Carlos"
            mock_registrar.return_value = True
            retorno = atender_proximo_cliente()
            assert retorno == "Atendimento realizado"

def test_fila_vazia():
    with patch("Exercicio6.obter_proximo_cliente") as mock_obter_cliente:
        with patch("Exercicio6.registrar_atendimento") as mock_registrar:
            mock_obter_cliente.return_value = None
            retorno = atender_proximo_cliente()
            assert retorno == "Fila vazia"

def test_falha_ao_registrar_atendimento():
    with patch("Exercicio6.obter_proximo_cliente") as mock_obter_cliente:
        with patch("Exercicio6.registrar_atendimento") as mock_registrar:
            mock_obter_cliente.return_value = "Carlos"
            mock_registrar.return_value = False
            retorno = atender_proximo_cliente()
            assert retorno == "Falha no atendimento"

def test_obter_proximo_cliente_foi_chamada():
    with patch("Exercicio6.obter_proximo_cliente") as mock_obter_cliente:
        with patch("Exercicio6.registrar_atendimento") as mock_registrar:
            mock_obter_cliente.return_value = "Carlos"
            mock_registrar.return_value = True
            atender_proximo_cliente()
            mock_obter_cliente.assert_called_once()

def test_registrar_atendimento_chamada_com_cliente_correto():
    with patch("Exercicio6.obter_proximo_cliente") as mock_obter_cliente:
        with patch("Exercicio6.registrar_atendimento") as mock_registrar:
            mock_obter_cliente.return_value = "Carlos"
            mock_registrar.return_value = True
            atender_proximo_cliente()
            mock_registrar.assert_called_once_with("Carlos")

def test_registrar_atendimento_nao_chamada_com_fila_vazia():
    with patch("Exercicio6.obter_proximo_cliente") as mock_obter_cliente:
        with patch("Exercicio6.registrar_atendimento") as mock_registrar:
            mock_obter_cliente.return_value = None
            atender_proximo_cliente()
            mock_registrar.assert_not_called()
