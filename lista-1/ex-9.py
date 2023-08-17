#Escreva um programa que pergunte a quantidade de km percorridos
#por um carro alugado pelo usuário, assim como a quantidade de dias
#pelos quais o carro foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

quantidade_percorrida = float(input('Quantos km foram percorridos: '))                  
dias = int(input('Quantos dias foram o aluguel: '))
total_pagar = dias * 60 + quantidade_percorrida * 0.15
print (f'O preço a pagar por {dias} dias e {quantidade_percorrida} km rodados é de R${total_pagar}')
