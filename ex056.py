soma = 0
old = 0
oldname = 0
new = 0
for c in range(1, 5):
    print('----- {}° PESSOA -----'.format(c))
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).strip().upper()
    soma += age
    if c == 1 and sex == 'M':
        old = age
        oldname = name
    if sex == 'M' and age > old:
        old = age
        oldname = name
    if age < 20 and sex == 'F':
        new += 1
media = soma / 4
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(old, oldname))
print('Ao todo são {} mulheres com menos de 20 anos'.format(new))
