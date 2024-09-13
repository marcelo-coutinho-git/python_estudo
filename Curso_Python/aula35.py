# Set (Listas)
    # Similar a listas
    # Evita Itens Duplicados
    # Nao utiliza index
    
lista1 = [10, 20, 30, 40, 50]
lista2 = [10, 20, 60, 70, 80]

num1 = set(lista1)
num2 = set(lista2)

s1 = {10, 20, 30, 40, 50}
s1.add(7)

print(s1)

print(num1 | num2) # Union - une as duas listas, removendo os valores repetidos
print(num1 - num2) # Difference - mostra apenas os numeros que nao sao repetidos
print(num1 ^ num2) # Symmetric Difference - Mostra os valores unicos
print(num1 & num2) #And - Mostra apenas os duplicados
print(len(num1)) # Mostra o tamanho da Lista