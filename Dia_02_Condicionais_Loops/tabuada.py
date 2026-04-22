while True:
    num = int(input("Qual é a tabuada que deseja: "))

    if num == -1:
        print("Programa encerrado.")
        break

    print(f"Tabuada de {num}")

    i = 0

    while i<=10:
        print(f"{i}*{num}={i*num}")
        i +=1

# O while True é usado para manter o programa em execução contínua,
# permitindo ao utilizador calcular várias tabuadas sem precisar reiniciar o programa.
# O loop só termina quando uma condição de saída (break) for ativada.