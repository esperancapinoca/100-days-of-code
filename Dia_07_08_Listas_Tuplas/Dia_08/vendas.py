

def total_vendas(vendas):
    total = 0
    for i in range(len(vendas)):
        total += vendas[i]
    return total

def media_vendas(vendas):
    return total_vendas(vendas)/len(vendas)

def melhor_dia(vendas):
    maior = vendas[0]
    indice = 0
    for i in range(len(vendas)):
        if vendas[i]>maior:
            indice = i
    return indice


vendas = [120, 85, 200, 95, 310]

opcaao = int(input("1. Total de Vendas\n2. Media das Vendas\n3. Melhor dia de Vendas "))

match opcaao:
    case 1: print(f"O total das vendas é: {total_vendas(vendas)}")
    case 2: print(f"A media das vendas é {media_vendas(vendas)}")
    case 3: print(f"O melhor dia de vendas é {melhor_dia(vendas)}")
    case _: print("OPÇÃO INVÁLIDA")
    