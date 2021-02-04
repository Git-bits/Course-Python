listagem = ('Lápis', 0.99,
            'Borracha', 0.50,
            'Caderno', 9.99,
            'Estojo', 5.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 19.99,
            'Caneta', 1.50,
            'Livro', 30.99)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')
print('-' * 40)
