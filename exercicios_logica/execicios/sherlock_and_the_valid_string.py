# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings# Complete the 'isValid' function below.

# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def isValid(s):
    word = {}
    list_s = list(s)
    values_frequence = {}
    
    for item in list_s:
        if item not in word:
            word[item] = 1
            
        else:
            word[item] = word[item] + 1

    for value in word.values():
        
        if value in values_frequence:
            values_frequence[value] += 1
            
        else:
            values_frequence[value] = 1
            
    if len(values_frequence) > 2:
        return "NO"
    
    count = 0
    
    for key, value in values_frequence.items():
        
        if values_frequence[key] > 1:
            count +=1
            
    if count > 1:
        return "NO"
        
    return "YES"


def isValid2(s):
    character_occurrences = {}
    
    for character in list(s):
        character_occurrences[character] = 1 if character not in character_occurrences else character_occurrences[character] + 1
       
    base_occurence = character_occurrences.values()[0]
    adjusts_left = 1

    for character_occurrence in character_occurrences:

        occurence_diff = character_occurrence - base_occurence 
        if occurence_diff > 1:
            return "NO"
        elif occurence_diff == 1 and adjusts_left > 0:
            adjusts_left = adjusts_left - 1
        

