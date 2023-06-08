from functions import *

print("#" * 40,'\n')
print("Qual a data de Vencimento?")
print("Formato: DIA-MES-ANO. Exemplo: 01-01-2000\n")
print("#" * 40,'\n')


due_date = input("")

if len(due_date) == 10:
    print(verify_due(due_date))
else:
    print("Entrada invalida! ")    