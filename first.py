def median3(a, b, c):
    x = a - b
    y = b - c
    z = a - c

    if x * y > 0: return b
    if x * z > 0: return c

    return a;