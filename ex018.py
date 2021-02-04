from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
co = cos(radians(ang))
tang = tan(radians(ang))
print('O ângulo de {:.1f} tem o SENO de {:.2f}'.format(ang, seno))
print('O ângulo de {:.1f} tem o COSSENO de {:.2f} '.format(ang, co))
print('O ângulo de {:.1f} tem o TANGENTE de {:.2f}'.format(ang, tang))
