import re

# It contains a minimum of 3 characters.
# It contains only digits (0-9), and English letters (uppercase and lowercase).
# It includes at least one vowel.
# It includes at least one consonant.


def isValid():
    # word = "234Aas" #true
    word = "Ya$"

    pattern = '[a-zA-Z0-9]'
    pattern_vowels = '[aeiouAEIOU]'
    pattern_consonant = '[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]'

    valid = False
    if len(word) >= 3 and word.isalnum():
        if re.search(pattern, word) and re.search(pattern_vowels, word) and re.search(pattern_consonant, word):
            valid = True

    return valid

print(isValid())