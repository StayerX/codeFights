def SumtheDifferenceV1(x):
    x = "#" + x.replace(" ", '')
    return sum([-int(x[i]) if (x[i - 1] == '-') ^ (int(x[i]) % 2) else int(x[i]) for i in range(1, len(x)) if
                x[i] in '123456789'])


def SumtheDifferenceV2(x):
    x = x.replace(' ', '')
    if len(x) == 0:
        return 0
    n = "0123456789"
    t = int(x[0]) if x[0] in n else 0
    t = t * -1 if t % 2 else t
    for p in range(1, len(x)):
        if x[p] in n:
            c = int(x[p])
            if x[p - 1] == '-':
                c *= -1
            if c % 2:
                c *= -1
            t += c
    return t
