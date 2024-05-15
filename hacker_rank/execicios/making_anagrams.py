# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b


def create_different_characters_list(dict_a, dict_b):
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


def makeAnagram(a, b):

    characters_a = list(a)
    characters_b = list(b)

    dict_str_a = {}
    dict_str_b = {}
    sum_difference = 0

    for character in characters_a:
        dict_str_a[character] = (
            1 if character not in dict_str_a else dict_str_a[character] + 1
        )

    for character in characters_b:
        dict_str_b[character] = (
            1 if character not in dict_str_b else dict_str_b[character] + 1
        )

    different_characters = create_different_characters_list(dict_str_a, dict_str_b)

    sum_difference = sum(different_characters.values())

    return sum_difference


makeAnagram("cde", "abc")


# TODO fazer função com for repetido em makeAnagram
# TODO fazer teste unitario para execicio 