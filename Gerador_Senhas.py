""" Gerador de Senhas """
print("="*20,'Gerador de Senhas',"="*20,'\n')

import random
import string

def gerador_senhas(len_senha = 8):
    ascii_opcao = string.ascii_letters    
    numero_opcao = string.digits
    punt_opcao = string.punctuation
    opcao = ascii_opcao + numero_opcao + punt_opcao

    senha_usuario = ''
    for i in range(0,len_senha):
         digito = random.choice(opcao)
         senha_usuario = senha_usuario + digito
    
    return senha_usuario


opcao_usuario = input('Quantos digitos na senha: ')

if opcao_usuario.isdigit():
    opcao_usuario = int(opcao_usuario)  
else:
    print('Entrada ivalida.')
    quit() 
    
reposta =  gerador_senhas(len_senha = opcao_usuario)        
print(f'Senha gerada:\n{reposta}')