print("CALCULADORA SIMPLES - Divisão")

dividendo = int(input("Digite o dividendo"))
divisor = int(input("Digite o divisor"))

quociente = dividendo//divisor
resto = dividendo%divisor

print(f"{dividendo} divido por {divisor} é igual a {quociente} onde tem como resto {resto}")