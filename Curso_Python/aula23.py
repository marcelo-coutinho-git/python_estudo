#Functions
    #DRY - Don't repeat yourself
    #Realizam uma tarefa
    #Calcula e retorna um valor
    
def cliente1(nome):
    print(f'Ola {nome}')
    
cliente1('Maria')
print(cliente1('Maria'))

def cliente2(nome):
    return f'Ola {nome}'

cliente2('Jose')
print(cliente2('Jose'))

