import random

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

lista = [a1, a2, a3, a4]
ordem = []

while lista:
    sorteio = random.choice(lista)
    ordem.append(sorteio)
    lista.remove(sorteio)
print(f'Aluno sorteado foi {ordem[0]}')
print(ordem)
