#Faça um programa para solicitar o nome e as duas notas e um aluno. Calcular sua média e informá-la.
# Se ela for inferior a 7, escrever "Reprovado”; caso contrário escrever "Aprovado".

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2
print('Media: ', media)

if media < 7.0:
    print('Reprovado')
else
    print('Aprovado')
