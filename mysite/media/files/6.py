def x_1(x1, x2, x):
    if x2 == 1998:
        if x1 == 1982:
            return x_3(x[1], x[3])
        elif x1 == 2016:
            return x_0(x[1], x[0])
        else:
            return x_3(x[1], x[3])
    elif x2 == 2017:
        if x1 == 1982:
            return x_0(x[1], x[0])
        elif x1 == 2016:
            return 11
        else:
            return 12
    else:
        return 8


def x_3(x1, x3):
    if x1 == 1982:
        if x3 == 'TOML':
            return 0
        elif x3 == 'MUPAD':
            return 1
        else:
            return 2
    else:
        if x3 == 'TOML':
            return 5
        elif x3 == 'MUPAD':
            return 6
        else:
            return 7


def x_0(x1, x0):
    if x1 == 2016:
        if x0 == 1988:
            return 3
        else:
            return 4
    else:
        if x0 == 1988:
            return 9
        else:
            return 10


def main(x):
    if x[4] == 'NCL':
        if x[2] == 1998 or x[2] == 2017:
            return x_1(x[1], x[2], x)
        else:
            return 8
    elif x[4] == 'MUPAD':
        return 13
    else:
        return 14

print(main([2008, 1982, 2017, 'MUPUD', 'NCL']))
print(main([1988, 2016, 2017, 'MUPAD', 'SHEN']))
