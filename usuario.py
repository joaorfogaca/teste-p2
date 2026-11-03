def buscar_usuario(usuario_id):
    return {
        "id":usuario_id,
        "nome":"Zoe Isabel",
        "idade":3
    }

def obter_nome(usuario_id):
    usuario = buscar_usuario(usuario_id)
    if(usuario["idade"] >= 3):
        return usuario["nome"]
    
    return usuario["id"]
