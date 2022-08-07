'''Na primeira etapa de um concurso, o candidato tem que fazer duas provas. Dessas duas notas é
tirada a média do candidato. Caso essa média seja maior ou igual a 7.0, ele estará apto a fazer a
segunda etapa do concurso. Na segunda etapa, ele fará mais uma prova, onde deverá obter uma
nota maior ou igual a 8.0 para ser aprovado no concurso.
Escreva um programa que leia as notas da primeira etapa, calcule a média da primeira etapa, e
se o candidato for aprovado na primeira etapa, leia a nota dele na segunda etapa e diga se ele
foi aprovado ou não no concurso.'''

nota1=float(input('1º nota da Primeira etapa: '))
nota2=float(input('2º nota da Primeira etapa: '))

media=(nota1+nota2)/2
print(f'Média: {media}')

if media >= 7:
    print('Parabéns! Você passou para Segunda etapa.')
    nota3=float(input('Nota da Segunda etapa: '))
    if nota3 >= 8:
        print('Aprovado!')
    else:
        print('Reprovado na Segunda etapa.')
else:
    print('Reprovado.')
