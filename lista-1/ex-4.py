salário = float(input('Digite seu salário: '))
porcentagem = float(input('Digite um aumento: '))
novo_salário = salário + salário * porcentagem / 100
aumento = novo_salário - salário

print (f'O aumento é de R${aumento}')
print (f'O novo salário é de R${novo_salário}')
