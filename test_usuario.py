from unittest.mock import patch
from usuario import obter_nome

def test_obter_nome():
    with patch("usuario.buscar_usuario") as mock_buscar_usuario:
        mock_buscar_usuario.return_value = {
            "id":1,
            "nome":"Carlos",
            "idade": 10,
            "test":"test"
        }
        nome = obter_nome(1)

        assert nome == "Carlos"
        mock_buscar_usuario.assert_called_once_with(1)

