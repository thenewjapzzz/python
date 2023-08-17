#1
x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
print (x + y)

#2
metros = int(input('Digite um valor em metros: '))
print (f'A medida de {metros} metros é igual a {metros*1000} milímetros')

#3
dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

total_em_segundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos
print (f'Convertido em segundos o total é {total_em_segundos} segundos')

#4
salário = float(input('Digite seu salário: '))
porcentagem = float(input('Digite um aumento: '))
novo_salário = salário + salário * porcentagem / 100
aumento = novo_salário - salário
print (f'O aumento é de R${aumento}')
print (f'O novo salário é de R${novo_salário}')

#5
mercadoria = float(input('Digite o valor da mercadoria: '))
porcentagem = float(input('Digite o valor do desconto: '))
novo_preco = mercadoria - mercadoria * porcentagem / 100
desconto = mercadoria - novo_preco
print (f'O valor do desconto é de R${desconto}')
print (f'O novo valor é de R${novo_preco}')

#6
distância = float(input('Informe a distância da viagem em quilômetros: '))
velocidade_média = float(input('Informe a velocidade média esperada: '))
tempo = distância / velocidade_média
print (f'O tempo da viagem é de {tempo} horas')

#7
c = float(input('Digite a temperatura em graus celsius: '))
f = 9*c/5 + 32
print (f'{c} ºC equivale a {f} ºF')

#8
f = float(input('Digite a temperatura em Fahrenheit: '))
c = (f - 32) * 5 / 9
print (f'{f}°F equivale a {c}°C')

#9
quantidade_percorrida = float(input('Quantos km foram percorridos: '))                  
dias = int(input('Quantos dias foram o aluguel: '))
total_pagar = dias * 60 + quantidade_percorrida * 0.15
print (f'O preço a pagar por {dias} dias e {quantidade_percorrida} km rodados é de R${total_pagar}')

#10
quantidade_diária = int(input('Quantos cigarros são fumados por dia: '))
anos_fum = int(input('Por quantos anos: '))
redução_minutos = anos_fum * 365 * quantidade_diária * 10
redução_dias = redução_minutos / 1440
print(f'Redução do tempo de vida em {redução_dias:.2f} dias')

#11
print (len(str(2**10000)))