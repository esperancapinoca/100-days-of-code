def soma(n1, n2): return n1 + n2
def subtracao(n1, n2): return n1 - n2
def multiplicacao(n1, n2): return n1 * n2
def divisao(n1, n2):
    return n1 / n2 if n2 != 0 else "Erro: Divisão por zero"

while True: 
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    print("Escolha a operação:\n1.Soma\n2.Subtração\n3.Multiplicação\n4.Divisão\n5.Sair")
    escolha = int(input("Opção: "))

    if escolha == -1:
        print("Sair")
        break
    
    match escolha:
        case 1:
            print(f"Resultado: {soma(num1, num2)}")
        case 2:
            print(f"Resultado: {subtracao(num1, num2)}")
        case 3:
            print(f"Resultado: {multiplicacao(num1, num2)}")
        case 4:
            print(f"Resultado: {divisao(num1, num2)}")
        case _:
            print("Opção Inválida")
