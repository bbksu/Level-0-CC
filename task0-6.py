def number_max(*args):
    hold = args[0]
    for value in args:
        if value > hold:
            hold = value
    max_value = hold
    return max_value
