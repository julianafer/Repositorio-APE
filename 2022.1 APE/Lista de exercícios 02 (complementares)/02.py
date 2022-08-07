'''Escreva um programa que solicite a digitação de um caractere qualquer do teclado e imprima
sua classificação: vogal, consoante, número e caractere especial.'''

c=input('Caractere: ').lower()

if c >= 'a' and c <= 'z':
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u' :
        tipo='vogal'
    else:
        tipo='consoante'
elif c >= '0' and c <= '9':
    tipo='número'
else:
    tipo='caractere especial'

print(f'Tipo: {tipo}')
