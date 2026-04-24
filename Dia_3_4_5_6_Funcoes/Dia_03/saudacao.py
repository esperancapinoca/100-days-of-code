from datetime import datetime

def saudar(nome, hora):
    if hora < 12:
        return f"Bom dia, {nome}"
    elif hora < 18:
        return f"Boa tarde, {nome}"
    else:
        return f"Boa noite, {nome}"

nomeInput = input("Digite seu nome: ")
hora_atual = datetime.now().hour

#fazemos o uso da função
print(saudar(nomeInput, hora_atual))