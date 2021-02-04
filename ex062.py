print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
total = 0
plus = 10
while plus != 0:
    total += plus
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    plus = int(input('Quantos termos você quer a mais?'))
print('Progressão finalizada com {} termos mostrados'.format(total))
print('FIM')
