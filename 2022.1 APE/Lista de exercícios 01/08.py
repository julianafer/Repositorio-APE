'''Faça um programa que leia o nome de um aluno e as notas das três provas que ele
obteve no semestre. No final informar o nome do aluno e a sua média (aritmética).'''
nome=(input('Olá!! Qual é o seu nome? '))
nota1=float(input('Informe sua primeira nota: '))
nota2=float(input('Informe sua segunda nota: '))
nota3=float(input('Informe sua terceira nota: '))
soma=nota1+nota2+nota3
média=soma/3
print(f'Olá {nome} sua média é {média}')
