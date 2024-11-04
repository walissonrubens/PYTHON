dias = int(input('Dias alugado: '))
km = int(input('Quilometros rodado: '))

pago = (dias * 60) + (km * 0.15)

print(f'Custo: {pago}')