import random

v = random.randint(1, 100)
#gera um número inteiro aleatório entre 1 e 100

while True:
    num = int(input("Digite um número: "))

    if num > v:
        print("Muito alto")
    elif num < v:
        print("Muito baixo")
    else:
        print(f"Parabéns esse é o número {v}")
        break