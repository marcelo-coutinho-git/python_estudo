# Erros 
    # Excelente para testes
    # Nao realiza o 'stop' no programa
    # Mensagens customizadas quando encontra um erro

try:
    letras = ['a', 'b', 'c']
    print(letras[3])
except IndexError:
    print('Index não existe')