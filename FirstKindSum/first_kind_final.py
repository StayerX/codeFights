from __future__ import generators
import decimal, math, numpy as np

br = np.binary_repr
prod = lambda bit: reduce(lambda x, y: x * y, bit)
sm = lambda bit: reduce(lambda x, y: int(x) + int(y), bit)
def rd(n,p):
    if len(n) == 1:
        return int(n)
    else:
        return int(n[-1]) + 2 * rd(n[:-1])
def rd(n,p):
    if len(n) == 1:
        return [int(n)*p]
    else:
        return  [p * int(n[-1])] + rd(n[:-1],p+1)


c = 0
s = 0
mx = ''.join(['1']*n)
cbr = br(s,n)
while mx != cbr:
    print cbr + " : " + str(rd(cbr,1))
    s += 1
    cbr = br(s, n)



def first_kind_sum_it_up(n, k):
    c = 0
    s = 0
    N = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    while c < N:
        s += 1
        print br(s)
        if sum(int(x) for x in br(s)):
            c += 1
    return ""


def xcomb(items, n):
    if n == 0:
        yield []
    else:
        for i in xrange(len(items)):
            for cc in xcomb(items[i+1:], n - 1):
                yield [items[i]] + cc