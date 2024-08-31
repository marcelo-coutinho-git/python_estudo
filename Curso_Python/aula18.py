# == While Loops ==
# Excelente para loops dependentes de uma cpndição.

# Criar uma promoção para um produto no valor de R100.

valor = 100
dia = 1

while valor > 20:
    dia +=1
    print(f'No dia {dia}, o produto vai ser vendido por R${valor}')
    valor-= 5