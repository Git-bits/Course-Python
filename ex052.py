p = int(input('Digite um número: '))
t = 0
for c in range(1, p + 1):
    if p % c == 0:
        print('\033[33m', end='')
        t += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(p, t))
if t == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
