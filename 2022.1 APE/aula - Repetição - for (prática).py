#Solicitar (n) números do usuário e a cada leitura mostar o dobro desse número
n=int(input('Digite a quantidade de números: '))
for i in range(n):
    numero=int(input('Digite um número: '))
    dobro=numero*2
    print(f'O dobro de {numero} é {dobro}')
print('Fim do programa')



#Solicitar (n) números do usuário e ao final da leitura mostrar a soma de todos os números lidos
n=int(input('Digite a quantidade de números: '))
somador=0
for i in range(n):
    numero=int(input('Digite um número: '))
    somador=somador+numero
print(f'Soma: {soma}')



#Fazer um programa para ler a nota de 5 alunos e dizer a quantidade de alunos aprovados (obs: o aluno aprovato teve nota maior ou superior a 70)
n=5
contador=0
for i in range(n):
    nota=int(input('Nota: '))
    if nota >= 70:
        contador+=1 #mesma coisa de contador=contador+1
print(f'{contador} aluno(s) aprovado(s)')
