# como rodar --> python3 list_slice.py (no terminal)

# para copiar uma lista pode-se usar new_list = list[:] isso vai garantir 
# que existam 2 listas diferentes e não duas variaveis apontando para a mesma lista

list_1 = [1,2,3,4,5]
list_2 = [6,7,8,9,10]

print("list_1 ", list_1)
print("list_2 ", list_2)

new_list = list_1[:]
new_list.append("Eu sou uma lista nova") # type: ignore

print("new_list ", new_list)

list_3 = list_2
list_3.append("Mema coisa da 2") # type: ignore
list_2.append("Isla bonita") # type: ignore 

print("list_2 ", list_2)
print("list_3 ", list_3)