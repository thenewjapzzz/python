#1
a = int(input('L1: '))
b = int(input('L2: '))
c = int(input('L3: '))
if (a + b < c) or (c + b < a) or (a + c < b):
    print ('Não é um triangulo')
elif (a == c) and (a == b):
    print ('Equilatero')
elif (a == b) or (b == c) or (a == c):
    print ('Isosceles')
else :
    print ('Escaleno')
#2
from calendar import isleap
ano = int(input('Ano:'))

if isleap(ano):
    print ('É bissexto')
else:
    print ('Não é bissexto')

#3
peso = int(input('Peso de peixe: '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    excesso = 0
    multa = 0

print (f'O excesso de peso foi de {excesso}kg e a multa de R${multa}')

#4
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))

if n1 > n2 and n1 > n3:
    print (n1)
elif n2 > n1 and n2 > n3:
    print (n2) 
else:
    print (n3)   

#5
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))

maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print (f'Maior {maior}')

menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print (f'Menor {menor}')
