registo = {}

def registar(registo, nome, senha):
    registo[nome] = senha #cria a chave nome com senha

#lembre, valor é associado a chave
# registo["maria"] isso é valor associado à chave "maria", ou seja: registo["maria"]  → "1234"

def fazer_login(registo, nome, senha):
    if nome in registo and registo[nome] == senha:
        #verifica se a senha guardada para aquele nome é igual à senha digitada        print("Login bem-sucedido")

        print("Login bem-sucedido")
    else:
        print("Nome ou senha incorretos")


def alterar_senha(registo, nome, senha_antiga, senha_nova):
    if nome in registo:
        if registo[nome] == senha_antiga:
            registo[nome] = senha_nova
            print("Senha alterada")
        else:
            print("Senha antiga errada")
    else:
        print("Usuário não existe")