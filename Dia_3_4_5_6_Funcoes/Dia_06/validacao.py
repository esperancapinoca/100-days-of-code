
def verificar_email(email):
    return "@" in email and "." in email

# uso:
"""
email = "teste@gmail.com"

if validar_email(email):
    print("EMAIL VÁLIDO")
else:
    print("EMAIL INVÁLIDO")
"""

# def verificar_email(email):
#     if "@" in email and "." in email:
#         print("EMAIL VÁLIDO")
#     else:
#         print("EMAIL INVÁLIDO")

def contar_palavras(texto):
    return len(texto.split()) # Separa o texto em palavras usando espaços e devolve o número total de palavras

"""
Primeiro o texto é dividido em palavras usando espaços como separadores.
Depois o len() conta quantas palavras existem na lista resultante.
Se não houver espaços, a lista terá apenas um elemento, e o resultado será 1.
"""

def verificar_idade (idade):
    return 18 <= idade <= 120

def validar_formulario(email, idade):
    if not verificar_email(email):
        return "Email inválido"
    
    if not verificar_idade(idade):
        return "Idade inválida"
    
    return True

def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0

    for letra in texto:
        if letra in vogais:
            contador += 1

    return contador    

def resumo_texto(texto):
    return {
        "palavras": contar_palavras(texto),
        "vogais": contar_vogais(texto)
    }    


r=validar_formulario("e@g.com", 18)
print(r)