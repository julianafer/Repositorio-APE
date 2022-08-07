'''Faça um programa que leia um número N, inteiro, e some todos os números
de 1 até N, mostrando o resultado.'''

n=int(input('Quantidade de números a serem somados: '))
soma=0
for i in range(1,n+1):
    soma=soma+i
    if i == n:
        print(i, end=' ')
    else:
        print(f'{i} + ', end='')
print(f'= {soma}')
