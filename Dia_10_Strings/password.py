password = input("Digite a palavra passe: ")

tem_maiuscula = False
tem_numero = False
tem_simbolo = False

for letra in password:
    if letra.isupper():
        tem_maiuscula = True
    elif letra.isdigit(): #se for número
        tem_numero = True
    elif not letra.isalnum():  # nem letra nem número
        tem_simbolo = True

if len(password) >= 8 and tem_maiuscula and tem_numero and tem_simbolo:
    print("Password válida")
else:
    print("Password inválida")