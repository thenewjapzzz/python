#Escreva um programa que leia a quantidade de dias,
#horas, minutos e segundos do usuário.
#Calcule o total em segundos.

dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

total_em_segundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos
print (f'Convertido em segundos o total é {total_em_segundos} segundos')
