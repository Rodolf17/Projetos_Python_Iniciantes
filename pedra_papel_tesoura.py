# Jogo do Pedra, papel e tesoura. 
import random

print('*' * 12)
#Pontuação do usuario e Pontuação do computador
user_points = 0
computer_points = 0 

options = ["r","t","p"]

while True:
    user_choice = input(
"""
Escolha: 
R-(Pedra)
T-(Tesoura)
P-(Papel)
ou Q para sair: """).lower()
    
    
    if user_choice == 'q':
        break
    
    if user_choice not in options:
        continue
        
        
    computer_choice = random.randint(0,2)
    # 0:Pedra(R) , 1:Tesoura(T) , 2:Papel(P)
    computer_options = options[computer_choice]
    
    print(f'O computador Escolheu : {computer_options}')
    
    if user_choice == computer_options: 
        print("Empate!🤡")
    elif user_choice == 'r' and computer_options == 't':
        print('Voce ganhou!😄')
        user_points = user_points + 1
        
    elif user_choice == 'p' and computer_options == 'r':
        print('Voce ganhou! 😄')
        user_points = user_points + 1 
        
    elif user_choice == 't' and computer_options == 'p':
        print('Voce ganhou!😄')
        user_points = user_points + 1         
    else:
        print("Você perdeu 😢.")
        computer_points = computer_points + 1



print("Sua pontuação: " + str(user_points))
print("Pontuação do Computador: " + str(computer_points))
if computer_points > user_points:
    print('Derrota!!😢')
elif computer_points == user_points:
    print("Empate!🤡")
else:
    print("Vitória!😄✅")        


print()        
print("GoodBye.")    