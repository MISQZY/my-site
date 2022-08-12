import math
def main(x, y):

    r = pow((66 * x * x + 72 * x * x * x), 4) -\
         42 * pow(math.exp(y * y * y / 85 + 62 + 67 * x), 7)
    r /= math.sin(x) - 73 * pow((y * y * y + 34), 7)
    r -= (64 * (9 * x + 1)) + pow((x * x * x + y * y + 14 * x), 4)

    return r