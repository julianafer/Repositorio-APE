'''Escreva um programa que receba um vetor V de N números inteiros (N será lido), determine e exiba o maior e o menor elemento deste vetor e seus respectivos índices.
Obs: suponha a inexistência de valores repetidos.'''

n = int(input('Quantidade de elemtos: '))
v = [None]*n
maior = 0
menor = 9999999999

for i in range(n):
  v[i] = int(input('Digite um número: '))

for i in range(n):
  if v[i] > maior:
    maior = v[i]
    a = i
  if v[i] < menor:
    menor = v[i]
    b = i

print(f'Maior: {maior} no índice {a}')
print(f'Menor: {menor} no índice {b}')
