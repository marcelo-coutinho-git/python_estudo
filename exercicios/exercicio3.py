"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


hora = input('Digite a Hora: ')


try: 
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print('Bom dia')
        
    elif hora > 11 and hora < 18:
        print('Boa Tarde')

    elif hora > 18 and hora <= 23:
        print('Boa noite')   
    else:
        print('Hora Invalida') 
except:
    print('Digitar hora em numero inteiro')