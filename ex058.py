from random import randint
computer = randint(0, 10)
print('''Sou seu computador... Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
cont = 0
hit = False
while not hit:
    player = int(input('Qual é o seu palpite? '))
    cont += 1
    if player == computer:
        hit = True
    else:
        if player < computer:
            print('Mais... Tente mais uma vez.')
        elif player > computer:
            print('Menos... Temte mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(cont))
