'''Escreva um programa que leia um vetor A de N números inteiros (N será lido) e
um outro inteiro K, construa e exiba um outro vetor B cujos elementos são os
respectivos elementos de a multiplicados por K.
Ex: A = [1,2,3], K = 5, B = [5,10,15].'''

n = int(input('Quantidade de elementos no vetor: '))
a = [None]*n
b = [None]*n

k = int(input('Multiplicador: '))

for i in range(n):
    a[i] = int(input(f'{i+1}º elemento do vetor: '))
    b[i] = a[i] * k

print('\nVetor A:')
print(a)

print('\nVetor B:')
print(b)
