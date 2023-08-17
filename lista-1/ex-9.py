quantidade_percorrida = float(input('Quantos km foram percorridos: '))                  
dias = int(input('Quantos dias foram o aluguel: '))
total_pagar = dias * 60 + quantidade_percorrida * 0.15
print (f'O preço a pagar por {dias} dias e {quantidade_percorrida} km rodados é de R${total_pagar}')
