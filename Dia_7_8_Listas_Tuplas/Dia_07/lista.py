
frutas = [ "manga","banana", "laranja", "papaia", "tomate"]

    #adiciona: frutas.append("limão")
    # #remover pela posição: frutas.remove(frutas[4])
    # #remover pelo nome: frutas.remove("manga")

    # #reverter frutas.reverse()

    # #índice negativo permite acessar a partir do fim da lista:
    # # print(frutas[-2])

    # #permite acessar os dois últimos elementos da lista print(frutas[-2:])

    # #ordena pelo tamanho das palavras frutas.sort(key=len)

    # frutas.sort()

print(frutas)

"""

def adicionar (f):
    frutas.append(f)

def remover (f):
    if f in frutas:
        frutas.remove(f)
    else:
        print("Essa fruta não existe")

  

frutas = [ "manga","banana", "laranja", "papaia", "tomate"]

opcao = int(input("1. Adicionar fruta\n2.Remover fruta por nome\n3.Listar frutas\n4.Ordenar"))

match opcao:
    case 1:
        fruta = input("Digite o nome da fruta: ")
        adicionar(fruta)
        print(frutas)
    case 2:
        fruta = input("Digite o nome da fruta: ")
        remover(fruta)
        print(frutas)
    case 3:
        print(frutas)
    case 4:
        frutas.sort(key=len)
        print("Frutas ordenadas:", frutas)
    case _:
        print("Opção Inválida")

"""