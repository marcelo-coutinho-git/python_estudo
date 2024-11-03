"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
lista_compras = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]Inserir [a]Apagar [l]listar: ').lower()
    
    if opcao == 'i':
        os.system('clear')
        produto = input('Digite um produto: ')
        lista_compras.append(produto)
        print(lista_compras)
    
    elif opcao == 'a':
        os.system('clear')
        deletar = int(input('Escolha o índice para apagar: '))
        
        try:
            del lista_compras[deletar]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
     
    elif opcao == 'l':
        os.system('clear')
        
        if len(lista_compras) == 0:
            print('Nada para listar')
            
        for i, valor in enumerate(lista_compras):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')
        