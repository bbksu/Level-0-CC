def n_max(*args):
    hold = 0
    for value in args:
        if value > hold:
            hold = value
    max_value = hold
    return max_value
