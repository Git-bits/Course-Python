print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)
produto = total = totmil = menor = cont = 0
barato = ''
while True:
    np = str(input('Nome do Produto: '))
    price = float(input('Preço: R$:'))
    total += price
    cont += 1
    if price > 1000:
        totmil += 1
    if cont == 1 or price < menor:
        menor = price
        barato = produto
    ask = ' '
    while ask not in 'SN':
        ask = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if ask == 'N':
        break
print('----------- FIM DO PROGRAMA ------------')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
