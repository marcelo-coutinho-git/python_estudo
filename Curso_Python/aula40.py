# Map Function
    # Muito utilizado com listas
    # Aplicar uma funcao a um Itarable, por item. (list, tuple, dic, etc)
    
    
lista1 = [1, 2,3 ,4]
# def multi(x):
#     return x * 2
# print(multi(2))

# lista2 = map(multi, lista1)
# print(list(lista2))

# lista2 = map(lambda X: x * 2, lista1)
print(list(map(lambda x: x * 2, lista1)))