'''Escreva um programa que leia um vetor de N números inteiros (N será lido), inverta a ordem dos elementos do vetor e exiba o vetor invertido. Ex: V = [1, 3, 5, 7], após a inversão: V = [7, 5, 3, 1].
Obs: É necessário inverter os elementos do vetor, não basta imprimi-los em ordem inversa!'''

n = int(input('Quantidade de elementos: '))
v = [None]*n

for i in range(n):
  v[i] = int(input('Digite um número: '))

for k in range(n//2):
  bob = v[k]
  v[k] = v[n-(k+1)]
  v[n-(k+1)] = bob

print(v)
