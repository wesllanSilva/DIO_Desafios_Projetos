valorHamburguer = float(input('Qual o valor do hamburguer?'))
quantidadeHamburguer = int(input('Qual a quantidade de hamburguer? '))
valorBebida = float(input('Qual o valor da bebida?'))
quantidadeBebida = int(input('qual a quantidade de bebida?'))
valorPago = float(input('qual o valor pago?'))



valorTotalHamburguer = valorHamburguer * quantidadeHamburguer
valorTotalBebida = valorBebida * quantidadeBebida
valorTotal = valorTotalBebida + valorTotalHamburguer
valorTroco = valorPago - valorTotal

print(f'O preço final do pedido é R$ {valorTotal:,.2f}. Seu troco é R$ {valorTroco:,.2f}.')


# Calcular o preço final do pedido (total dos hambúrgueres + total das bebidas).

# Calcular o troco do pedido, considerando o preço final e o valor pago pelo usuário.
# Imprimir a saída no formato especificado neste desafio.10.00