#Functions
    #DRY - Don't repeat yourself
    #Parametro --> Argumento
    #Default = Aquele que voce define o valor no parametro
    #Non-Default = Aquele que voce não define o valor no paramentro

def boas_vindas(nome, quantidade): #Paranetro
    print(f'Ola {nome}!')
    print(f'Temos {str(quantidade)} notebooks disponiveis')


boas_vindas('Marcelo', 4) #Argumento