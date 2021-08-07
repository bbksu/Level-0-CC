def vowels(string="Umuzi"):
    string = string.lower()
    vowels = ""
    for vowel in string:
        if vowel == 'A'.lower():
            vowels += vowel + ", "
        if vowel == 'E'.lower():
            vowels += vowel + ", "
        if vowel == 'I'.lower():
            vowels += vowel + ", "
        if vowel == 'O'.lower():
            vowels += vowel + ", "
        if vowel == 'U'.lower():
            vowels += vowel + ", "
    vowels = vowels.rstrip(", ")
    vowels = vowels + "."
    print("Vowels: ", vowels)
