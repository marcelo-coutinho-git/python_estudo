#Unpacking List
    #Armazenar mais de uma informcao em variavel
    #Manter a sequencia dos dados em uma variavel
    
produto = ['arroz', 'feijao', 'macarrao', 'laranja', 4, 3, 2, 1]

item1, item2, item3, *outros = produto

print(item1)
print(item2)
print(item3)
print(outros)