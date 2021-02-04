from random import randint
cont = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*20)
while True:
    pc = randint(0, 11)
    num = int(input('Diga um valor: '))
    soma = num + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = (input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print('-'*20)
    print(f'Você jogou {num} e o computador {pc}. Total de {soma}', end=' ')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    print('-'*20)
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você GANHOU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você GANHOU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
print('=-'*20)
print(f'GAME OVER! Você venceu {cont} vezes.')
