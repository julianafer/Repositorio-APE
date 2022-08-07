'''Escreva um programa que leia um vetor V contendo N elementos inteiros (N será
lido) e um valor inteiro K, verifique e exiba se o K está ou não no vetor. Se estiver,
informe em que posição (índice).
Obs: K pode se repetir no vetor, nesse caso, mostre todas as posições onde o K
aparece.'''

n = int(input('Quantidade de elementos no vetor: '))

v = [None]*n
for i in range(n):
    v[i] = int(input(f'{i+1}º elemento do vetor: '))

k = int(input('Número que você quer saber se está no vetor: '))

esta = 'n'
for i in v:
    if v[i] == k:
        esta = 's'
        print(f'Achei {k} no índice ')

if esta == 'n':
    print(f'O número {k} não está no vetor')
