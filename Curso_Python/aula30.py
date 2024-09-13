#Listas
    #Armazenar mais de uma informcao em variavel
    #Manter a sequencia de dados em uma variavel
  
cor_cliente = input('Digite a cor desejada: ')  
cores = ['amarelo', 'azul', 'verde', 'vermelho']

if cor_cliente.lower() in cores: 
#Lower, coloca tudo que foi digitado em minusculo
    print('Em Estoque')
else:
    print('Indisponivel')
