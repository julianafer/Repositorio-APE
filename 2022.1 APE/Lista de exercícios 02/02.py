#Escreva um programa que leia dois números e exiba-os em ordem crescente.

print('Digite doois números inteiros: ')
n1=int(input())
n2=int(input())

print('Números em ordem crescente: ', end='')
if n1 > n2:
    print(n2, n1)
else:
    print(n1, n2)
