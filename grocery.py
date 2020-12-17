
carrinho = []

produtos = {
    'Morango' : 5,
    'Pera' : 3,
    'Maçã' : 2,
    'Banana' : 1.50,
    'Shimeji' : 8,
    'Lichia' : 10,
    'Queijo' : 19.90,
    'Requeijão' : 5.40,
            }

print('Os produtos de nossa loja são:\n')

for index, p in enumerate(produtos):

    print(f'{p} por R${produtos.get(p)}.')

produto_desejado = input('\nDigite o produto que deseja: ')

while produto_desejado != 'fim':

    if produto_desejado in produtos:

        carrinho.append(produto_desejado)

        print(f'\nProdutos comprados até agora: {", ".join(carrinho)}.')

        produto_desejado = input('\nDigite o produto que deseja (se não deseja mais comprar digite "fim): ')

    else:

        produto_desejado = input('\nNão temos esse produto...\nOlhe nosso catálogo e escolha o produto desejado(se não deseja mais comprar digite "fim): ')

preço = [produtos.get(valor) for valor in carrinho]

print(f'\nO valor da compra é de R${float(sum(preço)):.2f}.')