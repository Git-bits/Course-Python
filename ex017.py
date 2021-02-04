from math import hypot
n1 = float(input('Comprimento do cateto oposto: '))
n2 = float(input('Comprimento do cateto adjacente: '))
m = hypot(n1, n2)
print('A hipotenusa vai medir \033[31m{:.2f}\033[m!!!'.format(m))
