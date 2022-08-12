import math

def main(z):
    if z < 41:
        r = z / 5 + pow(z, 4)
    elif 41 <= z < 90:
        r = 1 - pow(math.exp(z), 2)
    elif 90 <= z < 110:
        r = z + pow(z, 3) + 1
    else:
        r = 58 * pow(math.exp(z), 2)

    return r