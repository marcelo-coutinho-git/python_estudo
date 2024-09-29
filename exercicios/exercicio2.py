"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um numero inteiro ')

try:
    numero_int = int(numero)
    resultado = numero_int % 2
    if resultado == 0:
        print(f'Numero {numero_int}, é Par')
    else:
        print(f'Numero {numero_int}, é Impar') 
    
except:
    print('Voce nao digitou um numero inteiro')
    
  
     

