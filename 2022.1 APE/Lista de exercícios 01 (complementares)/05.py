'''Escreva um programa que, dado um número inteiro representando uma quantidade de
segundos, calcule quantas horas, minutos e segundos estão contidos nesta quantidade.
Ex: 7.388 segundos = 2 horas, 3 minutos e 8 segundos.'''
tempo=int(input('Segundos: '))
horas= tempo//3600
resto_h=tempo%3600
minutos=resto_h//60
resto_min=resto_h%60
segundos=resto_min
print()
print(horas,'horas')
print(minutos,'minutos')
print(segundos,'segundos')
