#List Comprehension
    # Mais simples de escrever
    # Quando voce precisa criar uma nova lista, a partir de uma existente
    # [expressa for item in itens]
    
#Criar uma lista apenas com as frutas que contenham a letra B

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']

# frutas2 = []
# for itens in frutas1:
#     if 'b' in itens:
#         frutas2.append(itens)

frutas2 = [iten for iten in frutas1 if 'b' in iten]

print(frutas2)        
