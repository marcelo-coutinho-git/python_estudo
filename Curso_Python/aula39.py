# Lambda Function
    # É uma função (pequena) sem nome
    # Pode ter vários argumentos mas somente 1 expressão
    # Muito utilizada dentro de outras funções
    # Código mais 'clean'

# x =  int(input('digite um numero: '))
# def somar(x):
#     return x + 10
# print(somar(x))

x =  int(input('digite um numero: '))
somar10 = lambda x: x + 10 
print(somar10(x))