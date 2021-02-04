casa = float(input('Qual é o valor da casa: R$'))
salario = float(input('Quanto de salário tens? '))
anos = int(input('Em quantos anos de financiamento?? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('-=-'*15)
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print('a prestação será de R${:.2f}'.format(prestacao))
print('-=-'*15)
if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('emprestimo NEGADO!')
