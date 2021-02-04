num = int(input('Me diga um número qualquer: '))
resultado = num % 2     # 0 = PAR | 1 = IMPAR
if resultado == 0:
    print('o número {} é \033[34mPAR'.format(num))
else:
    print('o número {} é \033[34mIMPAR'.format(num))
