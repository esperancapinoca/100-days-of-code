
def criar_sala(filas, colunas):
    sala = []
    for i in range(filas):
        linha = []
        for j in range(colunas):
            linha.append("livre")
        sala.append(linha)
    return sala

def reservar_assento(sala, fila, coluna):
    if sala[fila][coluna] == "livre":
        sala[fila][coluna] = "ocupado"
    else:
        print("Assento já está ocupado!")

sala = criar_sala(3, 4)
reservar_assento(sala, 1, 2)
for linha in sala:
    print(linha)


