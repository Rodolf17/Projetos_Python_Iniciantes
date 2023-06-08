import math
"ARARA"
 
def is_palindromo(word):
    j = len(word) -1
    resultado = 0
    for i in range(len(word)):
        if word[i] == word[j]:
            resultado = resultado + 1
        if i >= j:
            break    
        j = j - 1
         
    if resultado == math.ceil(len(word)/2) :      
        return True
    else:
        return False    
    
def is_palidromo_recursivo(word):
    print(word)
    if len(word) <= 1:
        return True    
    else:
        return word [0] == word[-1] and is_palidromo_recursivo(word[1:-1])
    
    
words = ['arara','racecar','carro','cama','level']

for word in words:
    print(word)
    print(is_palidromo_recursivo(word))
    print('\n')   