#Verificar se idade minima de uma pessoa esta apta a votar ou nao nas eleiçoes


idade   =   int(input('Qual sua idade: '))

# if idade >= 16:
#     resultado = print('Voce esta Apto a votar')
# else:
#     resultado = print('Voce ainda nao esta elegivel a votacao')

resultado = 'Voto Permitido' if idade >= 16 else 'Voto não Permitido'

print(resultado)