# como rodar --> python3 list_comprehension.py (no terminal)

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_names = [
    "ana",
    "carlos",
    "vitor hugo",
    "jessica",
    "julia",
    "fabio",
    "gabriel",
    "henrique",
    "jaqueline",
    "marcos",
]
list_places = [
    "Guarulhos",
    "São Paulo",
    "Santo André",
    "Cotia",
    "Araraquara",
    "Lindoia",
    "Brasilia",
    "São Conrado",
    "Andradina",
    "Suzanapolis",
]


def odd_and_pair_numbers(list):
    pair_list = [item for item in list if (item % 2) == 0]
    odd_list = [item for item in list if not (item % 2) == 0]
    
    return pair_list, odd_list


# odd_and_pair_numbers(list_numbers)


def places_with_specific_letter(list, letter):
    places_list = [item for item in list if letter in item.lower()]

    return letter, places_list


# places_with_specific_letter(list_places, "p")
# places_with_specific_letter(list_places, "t")
# places_with_specific_letter(list_places, "a")


def capital_title_names(list):
    capitalize_names_list = [item.capitalize() for item in list]
    title_names_list = [item.title() for item in list]

    return capitalize_names_list, title_names_list


# capital_title_names(list_names)
