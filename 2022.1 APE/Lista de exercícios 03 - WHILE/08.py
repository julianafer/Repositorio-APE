'''O cardápio de uma casa de lanches, especializada em sanduíches, é dado a seguir.
CÓDIGO  NOME           PREÇO
 H      Hamburger      R$5,00
 C      Cheese Burger  R$6,00
 B      Cheese Bacon   R$7,00
 F      Cheese Frango  R$4,00

Faça um programa que leia o código e a quantidade de cada item comprado por um cliente (a leitura do código “X” indica o fim dos dados de entrada).
Ao final, calcule e exiba o total a pagar.'''

total = 0

while True:
    cod = input('Código: ').lower()
    if cod == 'X' or cod == 'x':
        break
    elif cod == 'h':
        cod = 5
    elif cod == 'c':
        cod = 6
    elif cod == 'b':
        cod = 7
    elif cod == 'f':
        cod = 4
    qtd = int(input('Quantidade: '))
    valor = cod * qtd
    total += valor

print(f'Total a pagar: R${total:.2f}')
