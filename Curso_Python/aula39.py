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

def somar(x):
    func2 = lambda x: x + 10 
    return func2(x) * 4
    
print(somar(x))