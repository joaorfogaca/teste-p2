def verificar_permissao(usuario):
    usuarios_permitidos = ["Carlos", "Ana"]
    return usuario in usuarios_permitidos

def acessar_sistema(usuario):
    if verificar_permissao(usuario):
        return "Acesso autorizado"
    return "Acesso negado"
