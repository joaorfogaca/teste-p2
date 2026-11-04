def gerar_codigo():
    codigo = 'USR-1234'
    return codigo

def criar_identificacao(nome):
    codigo = gerar_codigo()
    msg = f'Usuário {nome} cadastrado com código {codigo}.'
    return msg
