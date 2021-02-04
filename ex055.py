maior = 0
menor = 0
for c in range(1, 6):
    kg = float(input('Peso da {}° pessoa: '.format(c)))
    if c == 1:
        maior = kg
        menor = kg
    else:
        if kg > maior:
            maior = kg
        if kg < menor:
            menor = kg
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))
