# Desafio com If, Elif e Else

'''
Criar um prograna que dependendo da temperatura (em celius) do steak, ele retornara o ponto de cozimento em portugues.
O usuario devera fornecer a temperatura

Temperaturas - Cozimento
120ºF ou 48ºC - Selada
130ºF ou 54ºC - Ao Ponto para mal
140ºF ou 60ºC - Ao ponto
150ºF ou 65ºC - AO ponto para bem
160ºF ou 71ºC - Bem passada
'''


temperatura = int(input('Digite a temperatura da Carne? '))


if temperatura < 48: 
    print('Deixar a carne Cozinhar por mais tempo')

elif temperatura in range (48, 53):
    print('Selada')
    
elif temperatura in range (54, 59):
    print('Ao ponto para mal')

elif temperatura in range (60, 64):
    print('Ao Ponto')
    
elif temperatura in range (65, 70):
    print('Ao ponto para Bem')
    
elif temperatura >= 71:
    print('Bem passada')

else: 
    ()
    
