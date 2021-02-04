n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('---'*18)
print('Com as notas {} e {}, a média do aluno foi {:.1f}'.format(n1, n2, media))
print('---'*18)
if media < 5.0:
    print('O aluno está REPROVADO')
elif media < 7:
    print('O aluno está em RECUPERAÇÃO')
else:
    print('O aluno está APROVADO')
