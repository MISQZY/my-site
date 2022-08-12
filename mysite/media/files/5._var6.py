import math

def main(x, y):
    s = 0
    n = len(x)
    for i in range(len(x)):
        s += y[i // 2] ** 3 - 10 * x[n - 1 - i] - y[i // 2] ** 2 / 17

    return s