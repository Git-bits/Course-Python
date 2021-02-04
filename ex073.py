times = ('Internacional', 'Flamengo','Atlético-MG', 'São Paulo',
         'Fluminense','Palmeniras', 'Grêmio', 'Athletico-PR',
         'Ceará SC', 'Corinthians', 'Santos', 'Atlético-GO')
print('-=' * 35)
print('Lista de times do Brasileirão: ', end='')
for t in times:
    print(t, end=', ')
print('\n', '-='*35)
print(f'Os 5 primeiros times são {times[0:5]}')
print('-=' * 35)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 35)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 35)
print(f'O Flamengo está na {times.index("Flamengo") + 1}° posição')
