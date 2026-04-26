# Sets de países
africa = {"Moçambique", "Angola", "África do Sul", "Quénia"}
europa = {"Portugal", "Espanha", "França", "Angola"}

# União (todos os elementos, sem repetir)
uniao = africa | europa

# Interseção (elementos comuns)
intersecao = africa & europa

# Diferença (elementos só de um set)
dif_africa = africa - europa
dif_europa = europa - africa

# Diferença simétrica (elementos que não são comuns)
dif_simetrica = africa ^ europa

# Mostrar resultados
print("União:", uniao)
print("Interseção:", intersecao)
print("Diferença (África - Europa):", dif_africa)
print("Diferença (Europa - África):", dif_europa)
print("Diferença Simétrica:", dif_simetrica)