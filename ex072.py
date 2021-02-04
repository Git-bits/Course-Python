cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
        'dezesseis', 'dezesete', 'dezoito',
        'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end='')
    print('-'*35)
    print(f'Você escolheu o número {cont[num]}')
    print('-'*35)
    pergunta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while pergunta not in 'SN':
        pergunta = str(input('Tente novamente. Quer continuar? [S/N]: ')).upper().strip()[0]
    if pergunta == 'N':
        break
print('-'*35)
print('FIM DO PROGRAMA')
