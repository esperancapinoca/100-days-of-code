cidades = [
    ("Maputo", -25.96, 32.58),
    ("Lisboa", 38.72, -9.13),
    ("São Paulo", -23.55, -46.63),
    ("Nova York", 40.71, -74.00),
    ("Cairo", 30.04, 31.24)
]

#o key define a regra de ordenação, lambda é uma função pequena e rápida (sem nome) - ela diz:
#Para cada elemento, pega isto.
#Sem lambda teriamos:
#def pega_latitude(cidade):
   # return cidade[1]
#cidades.sort(key=pega_latitude)  
cidades.sort(key=lambda cidade: cidade[1])

print(cidades)