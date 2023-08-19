nome = str(input('Nome de usuário: '))
senha = str(input('Senha: '))
while nome == senha:
    print('ERRO:o nome de usuário não pode ser igual a senha')
    nome = str(input('Nome de usuário: '))
    senha = str(input('Senha: '))
