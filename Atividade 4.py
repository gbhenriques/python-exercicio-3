#Faça um programa que leia dois números e mostre qual o maior dos dois.
#O programa deve informar caso sejam iguais

n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero'))

if(n1 > n2):
    print('O numero maior é', n1)
if(n1 > n2):
    print('O menor numero é', n1)

if(n2 > n1):
    print('O numero maior é', n2)
if (n2 < n1):
    print('O menor numero é', n2)

if (n1 == n2):
    print('Os numeros são iguais')
