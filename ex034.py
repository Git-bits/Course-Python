n1 = int(input('Qual é o salário do funcionário? R$'))
if n1 <= 1250:
    novo = n1 + (n1 * 15 / 100)
    print('Quem ganhava {:.2f} passa a ganhar {:.2f} agora'.format(n1, novo))
else:
    novo = n1 + (n1 * 10 / 100)
    print('Quem ganhava {:.2f} passa a ganhar {:.2f} agora'.format(n1, novo))
