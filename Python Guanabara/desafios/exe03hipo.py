import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
hi = math.hypot(co, ca)
print(f'{hi:.2f}')
