#Sempre que o usuário informar um número o programa deverá mostrar o dobro desse número.

flag = 0
msg = 'Informe um número: '
n = int(input(msg))
while n != flag:
    d = n * 2
    print(f'O dobro de {n} é {d}')
    n = int(input(msg))
print('Fim do programa')



#Versão com saída formatada

preco_kg = 25.00
peso = float(input('Peso do prato (em Kg): '))

while peso < 0:
    print('Valor inválido. Digite novamente.')
    peso = float(input('Peso do prato (em Kg): '))

valor=peso*preco_kg
print(f'Valor a pagar: R${valor:.2f}')



#Exibir 10 vezes o nome IFPB

cont = 1
while cont <= 10:
    print(cont,'IFPB')
    cont += 1



#Exibir os números de 1 a 50

cont=1
while cont<=50:
    print(cont,end=' ')
    cont+=1



#Solicitar N números do usuário, verificar e exibir se o número é par ou ímpar

n = int(input('Quantos números? '))
cont = 0
while cont < n:
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        print('par')
    else:
        print('ímpar')
    cont+=1
print('Fim do programa')



# Solicitar N números do usuário (até que o usuário digite o número zero ou a soma dos números lidos seja maior do que 100)
# e ao final da leitura mostrar a soma de todos os números lidos

flag = 0
soma = 0
num = int(input('Digite um número: '))
while num != flag and soma <= 100:
    soma += num
    print(f'Soma = {soma}')
    if soma <= 100:
        num = int(input('Digite um número: '))
print('Fim do programa')
