# Neste projeto irei fazer um quiz de perguntas.
print("Seja muito bem vindo ao quiz do Rodolfo! 🎯")


answer_user = input("""Você Desejar começar? 
([S]im/[N]ão): """)
if answer_user != "S":
    quit()

score = 0


print("Començando...")
pergunta1 = [
    ("Quem desenvolveu o jogo Grand Theft Auto(GTA)?"),
    ("(A)-Rocktar Games"),
    ("(B)-Ubisoft Software"),
    ("(C)-Activisons") ,
    ("(D)-EA "),
]

for p in pergunta1:
    print(p,sep='\n')
answer_1 = input("Respostas: ")
if answer_1  == "A":
    print('PARABENS VOCE ACERTOU!! 👏👏')
    score = score + 1
else:
    print("INCORRETO ❌")    
    
print()    
    
pergunta2 =[
    ("Qual Bicho Transmite Doenças de Chagas?"),
    ("(A)-Abelha"),
    ("(B)-Barata"),
    ("(C)-Pulga") ,
    ("(D)-Barbeiro"),
]    
for p in pergunta2:
    print(p,sep='\n')
answer_2 = input("Respostas: ")
if answer_2  == "D":
    print('PARABENS VOCE ACERTOU!! 👏👏')
    score = score + 1
else:
    print("INCORRETO ❌")    

print()

pergunta3 = [
    ("Qual fruto é conhecido no norte e nordeste como 'Jerimum'?"),
    ("(A)-Caju"),
    ("(B)-Abóbora"),
    ("(C)-Chuchu") ,
    ("(D)-Côco"),
]    
for p in pergunta3:
    print(p,sep='\n')
answer_3 = input("Respostas: ")
if answer_3  == "B":
    print('PARABENS VOCE ACERTOU!! 👏👏')
    score = score + 1
else:
    print("INCORRETO ❌")
    
print()        

pergunta4 = [
    ("Qual o coletivo de Cães?"),
    ("(A)-Matilha"),
    ("(B)-Rebanho"),
    ("(C)-Alcateia") ,
    ("(D)-Manada"),
]    
for p in pergunta4:
    print(p,sep='\n')
answer_4 = input("Respostas: ")
if answer_4  == "A":
    print('PARABENS VOCE ACERTOU!! 👏👏')
    score = score + 1
else:
    print("INCORRETO ❌")    

print()        

pergunta5 = [
    ("Qual é o triangulo que tem todos os lados diferentes ?"),
    ("(A)-Equilátero"),
    ("(B)-Isóceles"),
    ("(C)-Escaleno") ,
    ("(D)-Trapézio"),
]    
for p in pergunta5:
    print(p,sep='\n')
answer_5 = input("Respostas: ")
if answer_5  == "C":
    print('PARABENS VOCE ACERTOU!! 👏👏')
    score = score + 1
else:
    print("INCORRETO ❌")    

print()        

pergunta6 = [
    ("Quem compôs o Hino da independência ?"),
    ("(A)-Dom Pedro 1"),
    ("(B)-Manuel Bandeira"),
    ("(C)-Castro alvez") ,
    ("(D)-Carlos Gomes"),
]    
for p in pergunta6:
    print(p,sep='\n')
answer_6 = input("Respostas: ")
if answer_6  == "A":
    print('PARABENS VOCE ACERTOU!! 👏👏')
    score = score + 1
else:
    print("INCORRETO ❌")    


print()
print(f"Quiz Acabou... Pontuação: {score}/6")    