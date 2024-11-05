from math import radians, sin, cos, tan

an = float(input('Digite o angulo: '))
seno = sin(radians(an))
print(f'O angulo de {an} tem o seno de {seno:.2f}')
cosseno = cos(radians(an))
print(f'O angulo de {an} tem o cosseno de {cosseno:.2f}')
tan = tan(radians(an))
print(f'O angulo de {an} tem o tan de {tan:.2f}')
