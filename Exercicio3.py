def validar_documento(documento):
    documento = documento.replace(".", "").replace("-", "")
    return len(documento) == 11 and documento.isdigit()
