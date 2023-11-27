#Calcular a redução do tempo de vida de um fumanete
#Pergunte a quantidade de cigarros fumados por dia e por quantos anos
#Considere que um fumante perde 10 minutos de vida a cada cigarro
#Calcule quantos dias o fumante perderá de vida

quantidade_diária = int(input('Quantos cigarros são fumados por dia: '))
anos_fum = int(input('Por quantos anos: '))
redução_minutos = anos_fum * 365 * quantidade_diária * 10
redução_dias = redução_minutos / 1440
print(f'Redução do tempo de vida em {redução_dias:.2f} dias')
