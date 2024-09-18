# Erros 
    # Excelente para testes
    # Nao realiza o 'stop' no programa
    # Mensagens customizadas quando encontra um erro
  
try:    
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('caracter invalido')
finally:
    print('codigo ok')    

# else: 
#     print('numero valido')
#     resultado = valor *2 
#     print(resultado)

    
    
print('mais codigo')
    
    
