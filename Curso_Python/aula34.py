#Array (Matriz)
    #Similar a listas
    #Melhor performance
  
from array import array
  
letras = ['a', 'b', 'c', 'd']
numeros_x = [1, 2, 3, 4]
numeros_y = [5, 6, 7, 8]

print(letras)
print(numeros_x)
print(numeros_y)
print()

letras = array('u',['a', 'b', 'c', 'd'])
numeros_x = array('i',[1, 2, 3, 4])
numeros_y = array('f',[5.1, 6.2, 7.3, 8.4])

print(letras)
print(numeros_x)
print(numeros_y)