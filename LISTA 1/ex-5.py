#Solicite o preço de uma mercadoria e o percentual de desconto.
#Exiba o valor do desconto e o preço a pagar

mercadoria = float(input('Digite o valor da mercadoria: '))
porcentagem = float(input('Digite o valor do desconto: '))
novo_preco = mercadoria - mercadoria * porcentagem / 100
desconto = mercadoria - novo_preco

print (f'O valor do desconto é de R${desconto}')
print (f'O novo valor é de R${novo_preco}')
