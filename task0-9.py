def vowels(string="Umuzi"):
    string_1 = string
    string_2 = string
    vowel_list = list(set(string_1.lower()) & set(string_2.lower()))
    vowels = ""
    for vowel in vowel_list:
        if vowel == 'a':
            vowels += vowel + ", "
        if vowel == 'e':
            vowels += vowel + ", "
        if vowel == 'i':
            vowels += vowel + ", "
        if vowel == 'o':
            vowels += vowel + ", "
        if vowel == 'u':
            vowels += vowel + ", "
    vowels = vowels.rstrip(", ")
    vowels = vowels + "."
    print("Vowels: ", vowels)
