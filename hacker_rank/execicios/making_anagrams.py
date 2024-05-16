# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b

# TODO fazer teste unitario para execicio 

def create_list_excess_characters(dict_a, dict_b):
    different_characters = {}

    for character_a, value_a in dict_a.items():

        for character_b, value_b in dict_b.items():

            if character_a not in dict_b:
                different_characters[character_a] = value_a

            if character_b not in dict_a:
                different_characters[character_b] = value_b

    for character, value in dict_a.items():

        if character in dict_b:

            if dict_a[character] < dict_b[character]:
                different_characters[character] = dict_b[character] - value

            if dict_a[character] > dict_b[character]:
                different_characters[character] = value - dict_b[character]

    return different_characters

def create_character_dict(list):
    character_dict = {}

    for character in list:
        character_dict[character] = (
            1 if character not in character_dict else character_dict[character] + 1
        )
    
    return character_dict

def makeAnagram(a, b):

    characters_a = list(a)
    characters_b = list(b)

    dict_str_a = create_character_dict(characters_a)
    dict_str_b = create_character_dict(characters_b)

    sum_excess = 0

    excess_characters = create_list_excess_characters(dict_str_a, dict_str_b)

    sum_excess = sum(excess_characters.values())

    return sum_excess


print(makeAnagram("cde", "abc"))

