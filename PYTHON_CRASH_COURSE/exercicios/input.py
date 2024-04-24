# como rodar --> python3 input.py (no terminal)

msg = input("Escreva a menssagem:")

def eco(msg):
    list_msg = msg.split(" ")

    print(f'{msg}, {list_msg[-1]}, {list_msg[-1]}, {msg[-1]}')

eco(msg)

