print('='*20)
print('10 TERMOS DE UMA P A')
print('='*20)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = t + 10 * r
for c in range(t, d, r):
    print(c, '>', end=' ')
print('ACABOU')
