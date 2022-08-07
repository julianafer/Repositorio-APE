'''Faça um programa que leia os seguintes dados de um conjunto de alunos: matrícula, nome e as duas notas que ele obteve em suas avaliações.
A condição de parada será a digitação de uma matrícula igual 0 (zero).
O programa deverá mostrar, para cada aluno, as seguintes informações: matrícula, nome, média e situação
(aprovado, se a média for igual ou superior a 7 e, reprovado, se a média for inferior a 7).'''

flag=0
matricula=int(input('Matrícula: '))

while matricula != flag:
    nome=input('Nome: ')
    nota1=float(input('1ª Nota: '))
    nota2=float(input('2ª Nota: '))
    media=(nota1+nota2)/2
    if media >= 7:
        situ='aprovado'
    else:
        situ='reprovado'
    print(f'O(A) aluno(a) {nome} de matrícula {matricula} está {situ} com média {media:.1f}')
    print()
    matricula=int(input('Matrícula: '))

if matricula == 0:
    print('Matrícula inválida. Fim do programa')
