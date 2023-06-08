# Construindo jogo de Adivinhação Númerica em Python.
import random

print('Seja Muito bem vindo ao Guess Number do Rodolfo!')
choice_number = input('Digite o numero teto do desafio: ')

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print('Erro: valor informado não é numerico. favor execute novamente e informe um numero!')  
    quit()  
    
random_number = random.randint(0,choice_number)    
number_choices = 0

while True:
    answer_user = input('Adivinhe um numero: ')    
    if answer_user.isdigit():
        answer_user = int(answer_user)
    else: 
        print('Error: valor informado não é numérico. Favor informe um número!')
        continue
    number_choices = number_choices + 1
    if answer_user == random_number:
        print("Acertou 😃!")
        break    
    elif answer_user > random_number:
        print("Chutou alto, o número randomico é menor que isso...")
    else:
        print("Chutou baixo, o número randomico é maior que isso...")
            
print('N° de tentativas: ' + str(number_choices))    
    
    
    
    
    
    