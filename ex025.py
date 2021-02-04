nome = str(input('Qual é seu nome completo?: ')).strip()
print('Seu nome tem Silva? \033[34m{}\033[m'.format('SILVA' in nome.upper()))
