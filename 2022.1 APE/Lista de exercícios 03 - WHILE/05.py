'''Faça um programa que leia um número inteiro e determine se ele é par ou ímpar.
Ao final, o programa deve perguntar se o usuário deseja continuar (digitar outro número) ou sair.
Se o usuário quiser continuar, o programa deve repetir tudo de novo, caso contrário o programa deve ser encerrado.'''

numero = int(input('Digite um número inteiro: '))
if numero % 2 == 0:
    print(f'{numero} é par')
else:
    print(f'{numero} é ímpar')
continuar = input('Deseja continuar(sim ou não)? ').lower()

while continuar == 'sim':
    numero = int(input('Digite outro número inteiro: '))
    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é ímpar')
    continuar = input('Deseja continuar(sim ou não)? ').lower()
    
print('Fim do programa')
