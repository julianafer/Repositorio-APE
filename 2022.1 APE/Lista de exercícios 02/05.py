'''A empresa Vende Tudo Ltda paga o salário de cada vendedor
com uma comissão de 5% sobre o total de vendas daquele vendedor,
mas essa comissão nunca deve ser inferior ao salário-mínimo.
Escreva um programa que leia o valor total das vendas
de um vendedor e escreva seu salário.'''

porcentagem=5/100
minimo=1212

total=float(input('Valor total das vendas: '))
comissao=porcentagem*total
salario=minimo+comissao

print(f'Salário R${salario:.2f}')
