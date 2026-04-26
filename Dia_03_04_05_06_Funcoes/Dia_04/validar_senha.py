def validar_senha(senha):
    if len(senha) >= 8:
        return True
    else:
        return False


password = input("Digite a sua senha: ")

resultado = validar_senha(password)
print(resultado)

"""
def validar_senha(senha):
return len(senha) >= 8

#Funciona porque len(senha) >=8 é uma expressão lógica - essa comparação sempre resulta em um valor booleano (true/false)
"""