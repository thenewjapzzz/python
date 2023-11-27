#Faça um programa que leia um nome de
#usuário e a sua senha e não aceite a senha igual ao
#nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = str(input('Nome de usuário: '))
senha = str(input('Senha: '))
while nome == senha:
    print('ERRO:o nome de usuário não pode ser igual a senha')
    nome = str(input('Nome de usuário: '))
    senha = str(input('Senha: '))
