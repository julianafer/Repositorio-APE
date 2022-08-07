'''Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele próprio.
Faça um programa que mostre todos os números primos de 1 a N (obs: N será lido).'''

primo=True
pri=0

n=int(input('Número: '))

for i in range(n):
    if n%i == 0:
        primo=False
    if primo:
        pri+=1

print(f'{pri} números primos')
