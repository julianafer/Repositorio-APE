'''Faça um programa que, para um grupo de N pessoas (obs: N será lido):
• Leia o sexo (M ou F) de cada pessoa;
• Calcule e escreva o percentual de homens;
• Calcule e escreva o percentual de mulheres.'''

n=int(input('Quantidade de pessoas: '))
homem=0
mulher=0
for i in range(1,n+1):
    sexo=input(f'Sexo da {i}º pessoa (M ou F): ').upper()
    if sexo=='M':
        homem+=1
    else:
        mulher+=1
        
x=int((homem*100)/n)
y=int((mulher*100)/n)

print(f'{x}% homens e {y}% mulheres')
