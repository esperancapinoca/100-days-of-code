from datetime import datetime

# pedir data de nascimento
dia = int(input("Dia de nascimento: "))
mes = int(input("Mês de nascimento: "))
ano = int(input("Ano de nascimento: "))

hoje = datetime.today()


nascimento = datetime(ano, mes, dia)
dias_vividos = (hoje - nascimento).days

# próximo aniversário
ano_atual = hoje.year
proximo_aniversario = datetime(ano_atual, mes, dia)



print("Dias vividos:", dias_vividos)
print("Dias até o próximo aniversário:", proximo_aniversario)