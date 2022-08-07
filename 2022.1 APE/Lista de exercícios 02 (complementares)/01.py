'''Escreva um programa que solicite a digitação de um número (de 1 a 7) correspondente a um dia da semana e imprima o nome
do dia da semana e se é dia útil (de segunda a sexta) ou final de semana (sábado e domingo). Considere que o dia 1 é o domingo.'''

n=int(input('Número do dia da semana (1 a 7): '))

if n==1:
    dia='Domingo'
    util='fim de semana'
elif n==2:
    dia='Segunda-feira'
    util='dia útil'
elif n==3:
    dia='Terça-feira'
    util='dia útil'
elif n==4:
    dia='Quarta-feira'
    util='dia útil'
elif n==5:
    dia='Quinta-feira'
    util='dia útil'
elif n==6:
    dia='Sexta-feira'
    util='dia útil'
else:
    dia='Sábado'
    util='fim de semana'

print(f'{dia} ({util})')
