#Faça um programa que calcule o aumento de um salário.
#Ele deve solicitar o valor do salário e a porcentagem
#do aumento. Exiba o valor do aumento e do novo salário.

salário = float(input('Digite seu salário: '))
porcentagem = float(input('Digite um aumento: '))
novo_salário = salário + salário * porcentagem / 100
aumento = novo_salário - salário

print (f'O aumento é de R${aumento}')
print (f'O novo salário é de R${novo_salário}')
