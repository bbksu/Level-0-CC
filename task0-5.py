def area_of_triangle(side_a, side_b, side_c):
    semi_perimeter = (side_a + side_b + side_c) / 2
    heron = semi_perimeter * (
        (semi_perimeter - side_a)
        * (semi_perimeter - side_b)
        * (semi_perimeter - side_c)
    )
    heron = heron ** 0.5
    area = heron
    return area
