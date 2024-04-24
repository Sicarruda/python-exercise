# como rodar --> python3 functions.py (no terminal)


# name_user = input("Seu nome ")
# age_user = int(input("Sua Idade "))

# Positional Arguments -> argumentos que devem ser passados na ordem correta
def user_data(name, age):
    print(name, age)

# user_data(name_user, age_user)

# keyword argumentes -> argumentos são passados como nome-valor fazendo com que a posição não importe)
# When you use keyword arguments, be sure to use the exact names of the parameters in the function’s definition.
def user_data_2(name, age):
    print(name, age)

# user_data_2(age = age_user, name = name_user)

# When writing a function, you can define a default value for each parameter name = Jesssica
def user_data_3(name = "jessica" , age = 32):
    print(name, age)

# user_data_3()

# os argumentos pré definidos devem vir depois dos não definidos
def user_data_4(name, age, pet_name = "Ruby" ):
    print(name, age, pet_name)

# user_data_4(name_user, age_user)

toppings = ['mushrooms', 'green peppers', 'extra cheese']

# Envia uma copia do array envez do arrey em si podendo ser modificado sem prejuizo do original  
def make_pizza(toppings):
    toppings.append('lala')
    print(toppings)

# make_pizza(toppings[:])
# print(toppings)

# Quando não se sabe a quantidade de argumentos que serão enviados para a função pode-se usar o *, ele cria uma tupla com os valores passados
def make_pizza_2(*toppings):
    print(toppings) 

# make_pizza_2('mushrooms', 'green peppers', 'extra cheese', 'lala', 'lulu',  'lili')

# Misturando Argumentos Posicional e Arbitrario 
def make_pizza_3(size, *toppings):
    print(toppings)
    print(size)

make_pizza_3('big','mushrooms', 'green peppers', 'extra cheese', 'lala', 'lulu',  'lili')

# Misturando argumentos Keyword e Arbitrarios criando um dicionario com os passados em **user_info

def profile(first_name, last_name, **user_info):
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name

    return user_info

print(profile('jessica', 'arruda', age = '32', location = 'Araraquara'))
