def common_letters(string_a="", string_b=""):
    letters = ""
    set_list = list(set(string_a.lower()) & set(string_b.lower()))
    print(set_list)
    for letter in set_list:
        letters += letter + ", "

    letters = letters.rstrip(", ")
    print("Common letters:", letters)
