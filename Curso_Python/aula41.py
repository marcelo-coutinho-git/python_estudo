# Filter Function
    # Muito utilizado com listas
    # Aplicar uma funcao a um Itarable, por item. (list, tuple, dic, etc)
 
 
valores = [10, 20, 30, 40, 50] 
    
def remover20(x):
    return x > 20

print(list(filter(remover20, valores)))