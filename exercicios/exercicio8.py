"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você  vai conferir se a letra digitada está na palavra secreta.
- Se a letra digitada estiver na palavra secreta; exiba a letra;
- Se a letra digitada não estiver na palavra secreta; exiba *.
- Faça a contagem de tentativas do seu usuário.
"""
import sys

palavra_secreta = "dado"
letra_correta = ''
tentativas = 0
max_tentativa = 5


print ("***Adivinhe a palavra***")


while True:
    letra_digitada = input('Digite uma Letra: ').lower()
    tentativas += 1
    
    if len(letra_digitada) >1:
        print('Digite apenas uma letra')
        continue
    
    if len(letra_digitada) <1:
        print('Nenhuma letra foi digitada')
        continue
    
    if tentativas == max_tentativa:
        print('Tentativas:', tentativas)    
        print('VOCE ATINGIU O NUMERO MAXIMO DE TENTATIVAS')
        sys.exit()
        
        
    if letra_digitada in palavra_secreta:
        letra_correta += letra_digitada
        
    else:
        print('Letra incorreta, tente novamente')
        continue
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_correta:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('A Palavra secreta é', palavra_formada)
    
    if palavra_formada == palavra_secreta:
        print('VOCE GANHOU!!!!')
        print('Tentativas:', tentativas)
        sys.exit()


