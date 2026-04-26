texto = "A Maria é uma menina que carrega um sonho. É esse sonho que lhe mantem em movimento, ao ponto dela sair de Gaza para Maputo."

print("Caracteres:", len(texto))

palavras = texto.split() #Divide o texto
print("Palavras:", len(palavras))

vogais = "aeiouAEIOU"
contador = 0

for letra in texto:
    if letra in vogais:
        contador += 1

print("Vogais:", contador)