#Faça um programa que leia 20 números inteiros, determine e mostre o maior deles.

n=20
maior=0

print(f'Digite os {n} números:')

for i in range(n):
    numero=int(input())
    if numero > maior:
        maior = numero

print(f'Maior numero: {maior}')
