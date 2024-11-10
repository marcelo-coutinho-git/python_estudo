"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF, multiplicando cada um dos valores por uma contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = [7,4,6,8,2,4,8,9,0]
mult = [10,9,8,7,6,5,4,3,2]

#Colete a soma dos 9 primeiros dígitos do CPF, multiplicando cada um dos valores por uma contagem regressiva começando de 10
valor = [x * y for x, y in zip(cpf, mult)]
print(valor)

# Somar todos os resultados e multioplicar por 10
valor2 = sum(valor * 10)
print(valor2)

#Obter o resto da divisão da conta anterior por 11
resto = valor2 % 11
print(resto)


while True:
    if resto > 9:
        resultado = 0
                
    else:
        resultado = resto
        

    if resultado == cpf[0] :
        print(f'Primeiro digito do CPF, {cpf[0]} é Valido')
        
    else:
        print('invalido')

    break  
    



