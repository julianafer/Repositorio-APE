'''Recomendam-se estudantes para bolsas de estudo em função de seu desempenho. A natureza das recomendações é baseada na seguinte tabela:

CONCEITO     RECOMENDAÇÃO
   A         fortemente recomendado
 B ou C      recomendado
   D         não recomendado

Escreva um programa que leia o nome e o conceito de um estudante e exiba o nome do estudante e sua respectiva recomendação.'''

nome=input('Nome: ')
conceito=input('Conceito: ').upper()

if conceito=='A':
    rec='fortemente recomendado'
elif conceito=='B' or conceito=='C':
    rec='recomendado'
else:
    rec='não recomendado'

print(f'Estudante {nome} foi {rec}(a)')
