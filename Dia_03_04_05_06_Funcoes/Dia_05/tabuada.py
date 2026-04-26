def tabela_multiplicacao(n):
    for i in range(1, n + 1):        # controla a tabuada (1 até n)
        print(f"\nTabuada do {i}:")
        
        for j in range(1, 11):       # multiplica de 1 até 10
            print(f"{i} x {j} = {i * j}")

numero = int(input("Digite um número: "))
tabela_multiplicacao(numero)