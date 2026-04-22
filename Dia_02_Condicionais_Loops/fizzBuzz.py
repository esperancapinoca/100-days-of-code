for i in range(1, 101):  # Começa no 1 e vai até o 100

    if i % 3 == 0 and i % 5 == 0:  # Primeiro o mais específico
        print(f"FizzBuzz {i}")

    elif i % 3 == 0:
        print(f"Fizz {i}")

    elif i % 5 == 0:
        print(f"Buzz {i}")

    else:  # Caso não seja múltiplo de nada
        print(i)

#Um número é múltiplo de 3 quando a divisão por 3 tem resto igual a 0 - o mesmo para os demais números

