def common_letters(string_a="", string_b=""):
    string_b = string_b.lower()
    string_a = string_a.lower()
    letters = ""
    if len(string_a) > len(string_b):
        for c in string_a:
            if c in string_b:
                letters = letters + c + ", "
    else:
        for c in string_b:
            if c in string_a:
                letters = letters + c + ", "

    final_letters = list(dict.fromkeys(letters))
    final_letters.remove(",")
    final_letters.remove(" ")

    letters = ""

    for char in final_letters:
        letters += char + ", "
    letters = letters.rstrip(", ")

    print(f"'Common letters: {letters}'")
