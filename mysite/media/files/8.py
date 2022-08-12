def main(s):

    s = s.replace('\n', ' ')

    d = {}

    k_1 = 0
    data = ''

    for i in range(len(s) - 1):

        if s[i] == "'":
            if k_1 == 0:
                k_1 = i + 1
            else:
                data = s[k_1:i]
                if s[i+1] == ' ':
                    if s[i+4] != ' ':
                        k_1 = i+4
                    else:
                        k_1 = i+5
                else:
                    k_1 = i+4

        if s[i:i+3] == '||,':

            if s[i-1] == ' ':
                d.setdefault(s[k_1:i-1], data)
                k_1 = 0
                data = ''
            else:
                d.setdefault(s[k_1:i], data)
                k_1 = 0
                data = ''

    return d
