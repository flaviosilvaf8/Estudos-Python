
# Publicar um produto de loja terceira, com juros de 10%, se o produto for acima de 20$

valorProduto = int(input('Qual o valor do produto: '))
juros = (10 * valorProduto) / 100

while valorProduto > 20:
    valorProduto = valorProduto + juros
    print(f' O valor do produto com juros ficará {valorProduto}')
    break


