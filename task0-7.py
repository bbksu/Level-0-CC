def celsius_to_fahrenheit(celsius):
    fahrenheit = 32 + (celsius * (9 / 5))
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius
