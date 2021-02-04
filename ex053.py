frase = str(input('Digite uma frase: ')).strip().upper()
separ = frase.split()
junt = ''.join(separ)
inverso = junt[::-1]
print('O inverso de {} é {}'.format(junt, inverso))
if inverso == junt:
    print('ESSA PORRA É IGUAL MANÉ AKKAAKKKA')
else:
    print('ESSA PORRA N É IGUAL N MANE AKSKSKS')
