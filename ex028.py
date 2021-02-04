from random import randint
from time import sleep
pc = randint(0, 5)
print('\033[32m-=-\033[m' * 20)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[32m-=-\033[m' * 20)
ask = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if ask == pc:
    print('\033[32mPARABÉNS! Você conseguiu me vencer!')
else:
    print('\033[31mGANHEI! Eu pensei no número {} e não no {}!'.format(pc, ask))
