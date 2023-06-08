""" Calculadora com While"""
print("="*20,'CALCULADORA',"="*20,'\n')

while True:
    numero1 = input("Digite um numero: ")
    numero2 = input("Digite outro numero:  ")
    operador = input("Digite o operador +-*/: ")
    
    numeros_validos = None
    num1_float = 0
    num2_float = 0
    try:
      num1_float = float(numero1)
      num2_float = float(numero2)
      numeros_validos = True
    except:
        numeros_validos = None
        
        
    if numeros_validos is None:
        print("Um dos ambos numeros digitados são invalidos.")    
        continue        
        
    operadores_permitidos = '+-*/'
    
    if operador not in operadores_permitidos:
        print('Operador Inválido')
        continue     
    
    if len(operador)> 1:
        print('Digite apenas um operador.')     
        continue
    
    print('Realizando Sua Conta. Confira o Resultado abaixo: ')    
    if operador == "+":
        print(f'{num1_float} + {num2_float} =',int(num1_float + num2_float))
    elif operador == "-":
        print(f'{num1_float} - {num2_float} =',int(num1_float - num2_float))
    elif operador == "*":
        print(f'{num1_float} * {num2_float} =',int(num1_float * num2_float))
    elif operador == "/":        
        print(f'{num1_float} / {num2_float} =', num1_float / num2_float)
    else:
        print('Nunca deveria chegar até aqui.')        
       
    sair = input("Desejar Sair? [s/n]: ").lower().startswith("s")
    
    if sair is True:
        break


