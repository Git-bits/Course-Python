from datetime import date
atual = date.today().year
adult = 0
child = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade < 18:
        child += 1
    else:
        adult += 1
print('TEM {} PESSOAS DE MENOR'.format(child))

print('TEM {} PESSOAS DE MAIOR RAPA'.format(adult))
