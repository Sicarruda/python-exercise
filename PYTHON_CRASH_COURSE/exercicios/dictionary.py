# como rodar --> python3 dictionary.py (no terminal)

dict_1 = {"a": 1, "b": 2, "c": 3, "d": 4}

dict_2 = {"nome": "jessica", "idade": 32, "nacimento": "04/12/1991"}

dict_3 = {"jan": 31, "fev": 28, "mar":31, "abr":30, "mai": 31}

# print(dict_1)
# print(dict_2)

del dict_1["d"]
# print(dict_1)

# o .get() impede que aja um erro caso a chave não exista no dicionario retornando o segundo valor caso ela não exista 
nome_usuario = dict_2.get("nome", "não cadastrado")
sobrenome_ususario = dict_2.get("sobrenome", "não cadastrado")

# print(nome_usuario)
# print(sobrenome_ususario)

dict_2["sobrenome"] = "Arruda"

# retorna as chaves e o valor em cada uma delas. 
for key, value in dict_2.items():
    print(f"{key}: {value}")

# ambos os codigos retornam o mesmo resultado. Por padrão o Python sempre roda as chaves em um for
for key in dict_2:
    print(key)
    
for key in dict_2.keys():
    print(key)

for item in dict_2.values():
    print(item)

# A set is a collection in which each item must be unique:
for item in set(dict_3.values()):
    print(f"{item}")
# When you see braces but no key-value pairs, you’re probably looking at a set.
