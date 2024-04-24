# como rodar --> python3 tuples.py (no terminal)

''' tuplas não podem ser alteradas uma vez declaradas, mas podem ser redefinidas
na sua totalidade '''

tupla = (5, 5)
tupla_com_1_elemento = (1,)
print(tupla, tupla_com_1_elemento)

# aqui estamos tentado alterar um elemento da tupla o que vai causar um erro
# tupla[0] = 5 
# print(tupla)

# aqui alteramos a tupla inteira
tupla = (6, 5)  
print(tupla)

tuples_foods = ("batata", "mascarrão", "aspargos", "vinagrete")

for i in tuples_foods:
    print(f"\n{i}")

tuples_foods = ("limonada", "mascarrão", "polvo", "vinagrete")

for i in tuples_foods:
    print(f"\n{i}")
