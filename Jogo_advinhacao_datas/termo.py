import json
import random

f = open("jogo_advinhacao_datas/words.json", encoding="utf8")

carregar = json.load(f)
perguntas_aleatorias = random.choice(list(carregar.keys()))

print("Ola,Seja Bem vindo!")
print("###############################")

numero_chances = 5
VENCER = False

while numero_chances > 0 and VENCER is not True:         
    print("Dica: " + carregar[perguntas_aleatorias])
    respota_usuario = input("Data: DDMMAAA\n=> ")
    print("#################### \n")
     
    if len(respota_usuario) != 8:
        print("Erro na entrada. A resposta deve conter 8 digitos.")
        continue
    if respota_usuario.isdigit():
        check = []
        pontuacao = 0
        for i in range(8):
            if respota_usuario[i] == perguntas_aleatorias[i]:
                check.append("✅")
                pontuacao = pontuacao + 1
            else:
                check.append("❌")
        print("Resposta: \n")            
        print("|".join(check))            
        print(" |".join(respota_usuario))
        print("#########################")
        
        if pontuacao == 8:
            VENCER = True                        
    else:
        print("Erro na entrada. A resposta deve ser uma data.")    
        continue
    numero_chances = numero_chances - 1

if VENCER == True:
    print("VITÓRIA!!!")
else:
    print("DERROTA!")
    print("A resposta era: " + perguntas_aleatorias )    

