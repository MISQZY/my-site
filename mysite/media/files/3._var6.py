def main(a, n, z):
    r = 0
    for k in range(1, n+1):
        for j in range(1, a+1):
            r += pow((61 * z * z * z - j * j / 25 - j), 6) +\
                 pow((20 * k - 1), 5)

    return r