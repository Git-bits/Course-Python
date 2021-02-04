from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computer = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA 
[ 1 ] PAPEL
[ 2 ] TESOURA''')
player = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 11)
print('''O computador jogou {}
O jogador jogou {}'''.format(itens[computer], itens[player]))
print('-=' * 11)
if computer == 0:
    if player == 0:
        print('EMPATE')
    elif player == 1:
        print('O Jogador GANHOU')
Qual é a sua jogada?     elif player == 2:
        print('O Computador GANHOU')
    else:
        print('Opção Invalida')
elif computer == 1:
    if player == 0:
        print('O Computador GANHOU')
    elif player == 1:
        print('EMPATE')
    elif player == 2:
        print('O Jogador GANHOU')
    else:
        print('Opção Invalida')
elif computer == 2:
    if player == 0:
        print('O Jogador Ganhou')
    elif player == 1:
        print('O Computador GANHOU')
    elif player == 2:
        print('EMPATE')
    else:
        print('Opção Invalida')
