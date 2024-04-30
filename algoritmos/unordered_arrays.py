import random

# cria o array desordenado
def create_unordered_array(array_len):
    unordered_array = []
    created_array = True

    while created_array:
        item = random.randrange(1, array_len)
        unordered_array.append(item)

        if len(unordered_array) == array_len:
            created_array = False

    return unordered_array

# TODO fazer unordered_array com list comprehension
