print('{:=^40}'.format(' LOJA '))
price = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
option = int(input('Qual é a opção? '))
if option == 1:
    total = price - (price * 10 / 100)
elif option == 2:
    total = price - (price * 5 / 100)
elif option == 3:
    total = price
    portion = price / 2
    print('Sua compra será parcelada em 2x de {:.2f}'.format(portion))
elif option == 4:
    total = price + (price * 20 / 100)
    totalport = int(input('Quantas parcelas? '))
    portion = total / totalport
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(totalport, portion))
else:
    total = 0
    print('Opção invalida. Tente novamente.')
print('Sua compra de {:.2f} vai custar {:.2f} no final.'.format(price, total))
