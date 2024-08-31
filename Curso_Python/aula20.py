# Publicar um produto com comissao de 10% se for acima de R20

valor = int(input('Digite o valor do seu Produto: '))

while  valor > 20:
    valor = (valor * 0.10) + valor
    print(f'O valor final do seu produto sera de R${valor}')
    break
    