carrinho = []
quantidades = []
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
        quantidade = input('Quantidade: ')
        carrinho.append(produto_desejado)

        while not quantidade.isnumeric():
            quantidade = input(('Você deve digitar um número. Quantidade: '))

        quantidades.append(int(quantidade))

        print('\nProdutos no carrinho:')
        for i in range(len(carrinho)):
            if quantidades[i] > 1:
                print(f'{quantidades[i]} {carrinho[i]}s')
            else:
                print(f'{quantidades[i]} {carrinho[i]}')

        produto_desejado = input('\nDigite o produto que deseja (se não deseja mais comprar digite "fim): ')

    else:
        produto_desejado = input('\nNão temos esse produto...\nOlhe nosso catálogo e escolha o produto desejado(se não deseja mais comprar digite "fim): ')

preço = [produtos.get(valor) for valor in carrinho]
preço_final = [preço[i]*quantidades[i] for i in range(len(preço))]

print(f'\nCarrinho:\n\t{ "Produto":^15}\t{"Quantidade".center(15)}\t{"Preço":>15}')

for i in range(len(preço_final)):
        print(f'\t{carrinho[i]:^15}\t{quantidades[i]:^15}\t{preço_final[i]:>15.2f}')

print(f'\nO valor total da compra é de R${float(sum(preço_final)):.2f}.')
