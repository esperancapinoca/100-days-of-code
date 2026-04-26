numeros = [2, 5, 8, 9, 1, 0, 4, 3, 6, 7, 10]

def soma(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma


def media(lista):
    return soma(lista) / len(lista)
#Soma de todos valores pela quantidade

def minimo(lista):
    menor = lista[0]

    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]

    return menor

def maximo(lista):

    maior = lista[0]

    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]

    return maior


print("Soma:", soma(numeros))
print("Média:", media(numeros))
print("Mínimo:", minimo(numeros))
print("Máximo:", maximo(numeros))