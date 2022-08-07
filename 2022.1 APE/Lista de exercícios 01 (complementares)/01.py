'''A Companhia de Carros Usados João Honesto paga seus empregados um salário de R$
1.000,00 por mês mais uma comissão de R$ 200,00 por cada carro vendido mais 5% do
valor da venda.
Escreva um programa que leia o nome, o número de carros vendidos e o valor total das
vendas de um vendedor, e calcule e exiba o seu salário.'''
nome=input('Olá! Qual é o seu nome? ')
carros=int(input('Quantos carros você vendeu? '))
vendas=float(input('Qual foi o valor total das vendas? '))
comissao=(carros)*200
porcentagem=5/100
salário=1000+comissao+(vendas*porcentagem)
print(f'Parabéns {nome}! Seu salário esse mês é de R${salário:.2f}')
