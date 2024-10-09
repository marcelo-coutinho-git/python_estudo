""" Calculadora com while """


while True:
    
    
    numero_1 = input('Digite o primeiro numero: ')
    if numero_1.isdigit() == True:
        num_1 = float(numero_1)
    else:
        print('Numero Invalido')
        break
    
    numero_2 = input('Digite o segundo numero: ')
    if numero_2.isdigit() == True:
        num_2 = float(numero_2)
    else:
        print('Numero Invalido')
        break
    
    operador = input('Digite o operador (+-/*): ')
    
    numeros_validos = None
    
    try:
  
        numeros_validos = True
        
    except:
        numeros_validos = None
             
    if numeros_validos is None:
        print('Um ou mais numeros digitados sao invalidos.')
        continue
    
    operadores_permitidos = '+-/*'
    
    if operador not in operadores_permitidos:
        print('Operador Invalido')
        continue
    
    if len(operador) > 1:
        print('Digite apenas 1 operador')
        continue

    #########
    
    if operador == '+':
        resultado = num_1 + num_2
        print(f'{num_1} {operador} {num_2} = {resultado}')
    
    elif operador == '-':
        resultado = num_1 - num_2
        print(f'{num_1} {operador} {num_2} = {resultado}') 
    
    elif operador == '*':
        resultado = num_1 * num_2
        print(f'{num_1} {operador} {num_2} = {resultado}') 
    
    elif operador == '/':
        resultado = num_1 / num_2
        print(f'{num_1} {operador} {num_2} = {resultado}')  
        
    ##########
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break
    
print('Obrigado!')