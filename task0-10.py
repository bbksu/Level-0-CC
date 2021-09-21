def common_letters(string_a="", string_b=""):
    letters = ""
    if len(string_a) > len(string_b):
        for c in string_a:
            if c in string_b:
                letters = letters + c + ", "
    else:
        for c in string_b:
            if c in string_a:
                letters = letters + c + ", "

    letters = letters.rstrip(", ")
    print(f"'Common letters: {letters}'")
