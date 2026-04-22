while True:
    
    num = int(input("Digite um número (-1 para sair): "))

    if num == -1:
        print("Programa encerrado.")
        break

    if num == 0:
        print("O número é zero")

    elif num % 2 == 0:
        print("O número é par")

    else:
        print("O número é ímpar")