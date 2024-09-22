# Desafio com Funções

'''
Criar um programa que calcula a quantidade de tinta necessaria para pintar uma parede. 
O usuario  devera fornecer as seguintes informaçoes: Rendimento, altura e largura
O programa deve mostrar na tela a mesngem 'Voce necessita de x latas de tinta'
'''

rendimento = int(input('Qual rendimento da lata: '))
altura     = int(input('Qual altura da parede: '))
largura    = int(input('Qual largura da parede: '))

def latas_de_tinta():
    resultado = (altura * largura)/rendimento
    print(f'Voce precisa de  {resultado}  latas de tinta' )
    
latas_de_tinta()
    