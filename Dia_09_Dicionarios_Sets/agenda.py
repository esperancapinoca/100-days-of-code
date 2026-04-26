
def adicionar():
    nome = input("Nome: ")
    contacto = int(input("Contacto: "))
    agenda.append({"nome": nome, "contacto": contacto})

def listar():
    for i, c in enumerate(agenda, start=1):
        print(f"{i}. {c['nome']} - {c['contacto']}")
#i = numeros 1, 2, 3...
#c = cada elemento da lista

def remover():
    nome = input("Nome a remover: ")
    for c in agenda:
        if c["nome"] == nome:
            agenda.remove(c)
            print("Removido com Sucesso")
        else:
    
            print("Não encontrado")

agenda = []

while True:
    print("\n1-Adicionar 2-Listar 3-Remover 4-Sair")
    op = int(input("Escolha: "))
    match op:
        case 1: adicionar()
        case 2: listar()
        case 3: remover()
        case 4: break
        case _: print("Opção INVÁLIDA")
