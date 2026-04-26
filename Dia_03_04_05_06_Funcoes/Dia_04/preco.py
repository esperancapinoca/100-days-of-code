def calcular_preco_final (p, d):
    return p-(p*d/100)

preco = float(input("Digite o Preço: "))

if preco < 0:
    print("Preço inválido! Não pode ser negativo.")
    exit()
desconto = float(input("Digite o desconto em porcentagem: "))



total = calcular_preco_final(preco, desconto)

print(f"Preço {preco} aplicado o desconto de {desconto} %\nO valor Total é {total}")