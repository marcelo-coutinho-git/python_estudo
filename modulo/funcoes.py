def somar():
    print('Essa funcao vai somar valores')
    
def multi():
    print('Essa funcao vai multiplicar os valores')
    
def find_index(to_find, item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return i
    return -1
    