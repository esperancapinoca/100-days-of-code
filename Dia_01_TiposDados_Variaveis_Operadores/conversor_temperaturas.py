print("CONVERSOR DE TEMPERATURAS")

celsius = int(input("Digite a temperatura em Celsius: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273

print(f"Celsiu para Fahrenheit é {fahrenheit}")
print(f"Celsiu para Kelvin é {kelvin}")

"""
def celFa(celsius):
    return (celsius * 9/5) + 32

def celKe(celsius):
    return celsius + 273

print("CONVERSOR DE TEMPERATURAS")

while True:
    op = int(input("\nEscolhe o tipo de conversão:\n1. Celsius para Fahrenheit\n2. Celsius para Kelvin\n3. SAIR\n"))

    match op:
        case 1:
            c = float(input("Digite os graus Celsius: "))
            print(f"{c}°C = {celFa(c)}°F")

        case 2:
            c = float(input("Digite os graus Celsius: "))
            print(f"{c}°C = {celKe(c)}K")

        case 3:
            print("Programa encerrado.")
            break

        case _:
            print("Opção inválida.")
"""

#While: enquanto essa condição for verdadeira continua repetindo - com break ela para
#while false quase nunca porque ele é literalmente um loop que nunca executa. "Enquanto for falso, executa" - Mas como já começa falso nem entra no bloco.