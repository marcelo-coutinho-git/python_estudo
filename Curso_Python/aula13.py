#For Loops - Utilizando If e Else

# Cenario, Enviar um email com os detalhes de compra on line (Maximo 3 tentativas) para compras confirmadas

compra_confirmada  =   False
dados_da_compra    =   'Çompra no valor de R$ 12,50 e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_da_compra)
        print('Detalhes enviados por email')
        break
else:
    print('Falha na Compra')

 