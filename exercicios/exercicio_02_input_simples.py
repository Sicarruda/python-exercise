'''Faça um Programa que peça um número e então mostre a mensagem O número
informado foi [número].'''

def formata_mensagem_usuario(valor):
    if type(valor) != int:
        raise TypeError('Valor não permitido')
    return ( f'O numero informado foi {valor}')
    

if __name__ == '__main__':
    numero = int(input('Digite um numero: '))
    print(formata_mensagem_usuario(numero))