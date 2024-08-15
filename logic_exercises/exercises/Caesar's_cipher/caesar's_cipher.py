# https://www.hackerrank.com/challenges/one-week-preparation-kit-caesar-cipher-1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-three

import os

# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s is a valid ASCII string without any spaces. 
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    new_str = ""
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    alphabet_upercase = []

    for element in alphabet:
        alphabet_upercase.append(element.upper())

    alphabet_rotated = []
    alphabet_upercase_rotated = []

    if k > 26:
        rotation = int(k % 26)
    elif k < 26:
        rotation = k
    else:
        rotation = 0

    if rotation:
        temp_list = []
        temp_list_uppercase = []

        for element in range(rotation):
            temp_list.append(alphabet[element])
            temp_list_uppercase.append(alphabet_upercase[element])

        for element in range(len(alphabet) - rotation):
            alphabet_rotated.append(alphabet[element + rotation])
            alphabet_upercase_rotated.append(alphabet_upercase[element + rotation])

        for element in range(len(temp_list)):
            alphabet_rotated.append(temp_list[element])
            alphabet_upercase_rotated.append(temp_list_uppercase[element])

    else:
        alphabet_rotated = alphabet
        alphabet_upercase_rotated = alphabet_upercase

    for char in range(len(s)):

        if s[char] in alphabet:
            index_str = alphabet.index(s[char])
            new_str = new_str + alphabet_rotated[index_str]

        elif s[char] in alphabet_upercase:
            index_str = alphabet_upercase.index(s[char])
            new_str = new_str + alphabet_upercase_rotated[index_str]

        else:
           new_str = new_str + s[char]

    return new_str


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + "\n")

    fptr.close()
