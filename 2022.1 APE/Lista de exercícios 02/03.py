#Escreva um programa que leia 3 números inteiros, determine e mostre o maior deles.

print('Digite 3 números inteiros: ')
n1=int(input())
n2=int(input())
n3=int(input())

if n1>n2 and n1>n3:
    print(f'{n1} é maior')
elif n2>n3: #não entendi essa parte
    print(f'{n2} é maior')
else:
    print(f'{n3} é maior')
