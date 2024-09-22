# Calculo de IMC - Indice de Massa Corporal

'''
Qual é a sua Altura em cm:
Qual é o seu peso em kg:

MENOR QUE 18,5 MAGREZA
ENTRE 18,5 E 24,9 NORMAL
ENTRE 25,0 E 29,9 SOBREPESO
ENTRE 30,0 E 39,9 OBESIDADE
MAIOR QUE 40,0 OBESIDADE GRAVE
'''

peso   = float(input('Qual é o seu peso em kg: '))
altura = float(input('Qual é a sua Altura em cm: '))

imc = peso / (altura/100)**2

print(f'Seu IMC é: {imc:.2f}')

if imc < 18.5:
    print('Magreza')
    
elif imc >=18.5 and  imc < 24.9:
    print('Normal')
    
elif imc >= 25.0 and imc < 29.9:
    print('Sobrepeso')
    
elif imc >= 30.0 < 39.9:
    print('OBESIDADE')
    
elif imc >= 40.0:
    print('OBESIDADE GRAVE')

