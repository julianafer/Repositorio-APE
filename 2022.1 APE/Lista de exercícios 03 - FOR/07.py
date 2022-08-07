'''Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele
próprio. Faça um programa que leia um número e determine se ele é ou não
primo.'''

primo=True

n=int(input('Número: '))

for i in range(2,n):
    if n%i == 0:
        primo=False

if not primo:
    print(f'{n} não é primo')

else:
    print(f'{n} é primo')
