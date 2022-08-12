import math

def main(n):
    if n == 0:
        return -0.39
    elif n >= 1:
        return math.sin(main(n - 1)) + pow(main(n - 1), 3)
