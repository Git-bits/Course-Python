person = man = woman = 0
while True:
    print('-'*20)
    print(' CADASTRE UMA PESSOA')
    print('-'*20)

    idade = int(input('Idade: '))
    if idade >= 18:
         person += 1

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if sexo == 'M':
        man += 1
    if sexo == 'F' and idade < 20:
        woman += 1

    ask = ' '
    while ask not in 'SN':
        ask = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if ask == 'N':
        break
print('FIM DO PROGRAMA')
print(f'Total de pessoas com mais de 18 anos: {person}')
print(f'Ao todo temos {man} homens cadastrados')
print(f'E temos {woman} mulheres com menos de 20 anos')
