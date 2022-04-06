'''Faça um Programa que peça um número e então mostre a mensagem O número
informado foi [número].'''

def print_mensagem_usuario(valor):
    return ( f'O numero informado foi {valor}')
    

if __name__ == '__main__':
    numero = int(input('Digite um numero: '))
    print_mensagem_usuario(numero)