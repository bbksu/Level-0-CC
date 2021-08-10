def common_letters(string_a="house", string_b="computers"):
    letters = ""
    set_list = list(set(string_a.lower()) & set(string_b.lower()))
    for letter in set_list:
        letters += letter + ", "

    letters = letters.rstrip(", ")
    print("Common letters:", letters)