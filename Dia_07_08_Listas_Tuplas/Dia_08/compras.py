def adicionar_item(carrinho, item, preco):
    produto = {"nome": item, "preco": preco}
    carrinho.append(produto)


def remover_item(carrinho, item):
    for produto in carrinho:
        if produto["nome"] == item:
            carrinho.remove(produto)
            return
    print("Esse produto não existe")


def ver_total(carrinho):
    total = 0
    for produto in carrinho:
        total += produto["preco"]
    return total


def limpar_carrinho(carrinho):
    carrinho.clear()


def contar_produtos(carrinho):
    return len(carrinho)


def verificar_existe(carrinho, item):
    for produto in carrinho:
        if produto["nome"] == item:
            return True
    return False


carrinho = []

while True:
    op = int(input(
        "\n1. Adicionar Produto"
        "\n2. Remover item"
        "\n3. Soma dos preços"
        "\n4. Limpar carrinho"
        "\n5. Número de produtos"
        "\n6. Verificar produto"
        "\n0. Sair\n"
    ))

    if op == 0:
        break

    match op:
        case 1:
            item = input("Nome: ")
            preco = float(input("Preço: "))
            adicionar_item(carrinho, item, preco)
            print(carrinho)

        case 2:
            item = input("Nome: ")
            remover_item(carrinho, item)
            print(carrinho)

        case 3:
            print("Total:", ver_total(carrinho))

        case 4:
            limpar_carrinho(carrinho)
            print("Carrinho limpo")

        case 5:
            print("Quantidade:", contar_produtos(carrinho))

        case 6:
            item = input("Nome: ")
            print(verificar_existe(carrinho, item))