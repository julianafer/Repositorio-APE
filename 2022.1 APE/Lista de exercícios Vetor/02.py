'''Escreva um programa que leia um vetor V (contendo 30 inteiros) e um valor
inteiro K, calcule e exiba a quantidade de ocorrências de K dentro de V.'''

n = 5
soma = 0
v = [None]*n

for i in range(n):
    v[i] = int(input(f'{i+1}º elemento do vetor: '))

k = int(input('Número que você quer saber quantas vezes aparece: '))

for i in v:
    if i == k:
        soma += 1

print(f'\nO número {k} aparece {soma} vezes')
