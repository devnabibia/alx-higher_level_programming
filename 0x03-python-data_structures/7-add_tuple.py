#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first two elements from each tuple
    a = tuple_a[:2]
    b = tuple_b[:2]

    # If a tuple is smaller than 2, append 0 to make it of length 2
    if len(a) < 2:
        a += (0,) * (2 - len(a))
    if len(b) < 2:
        b += (0,) * (2 - len(b))

    # Calculate the sum of corresponding elements and create a new tuple
    result = (a[0] + b[0], a[1] + b[1])

    return result

