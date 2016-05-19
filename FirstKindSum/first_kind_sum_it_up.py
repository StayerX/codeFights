import itertools, math, decimal
import numpy as np
from collections import MutableSequence, Iterable

mult = {}


def first_kind_sum_it_up(n, k, version):
    if version == 1:
        r = kbits(n,k,1)
    if version == 2:
        r = kbits2(n,k,1)
    if version == 3:
        r = kbits3a(n,k,1)
    if version == 4:
        r = kbits3f(n,k,1)
    if version == 5:
        r = kbits3b(n,k,1)
    if version == 6:
        r = kbits3d(n, k, 1)
    if version == 7:
        r = kbits3d(n, k, 1)
    div = max(r)*1.0
    res = sum([div/x for x in r])/div
    d = decimal.Decimal(res).as_tuple()
    pow = len(d.digits) + d.exponent - 1
    re = "%.2f" % round(res*math.pow(10,-pow),2)
    res = ('%sE+%d' % (re,pow)) if pow>=0 else ('%sE%d' % (re,pow))
    return res


def kbits(n, k, l):
    bits = itertools.combinations(range(1,n+1), k)
    return map(lambda bit: np.prod(bit),bits)


def kbits2(n, k, l):
    bits = itertools.combinations(range(1,n+1), k)
    return map(lambda bit: reduce(lambda x,y: x*y,bit),bits)


def kbits3(n, k, l):
    bits = itertools.combinations(range(1, n + 1), k)
    prod = lambda bit: reduce(lambda x, y: x * y, bit)
    mid = k / 2
    it = 0
    for bit in bits:
        p1 = prod(bit[0:mid])
        p2 = prod(bit[mid:])
        break
    return [p1*p2] + [p1 * prod(bit[mid:]) if it < mid else (bit)for bit in bits]


def kbits3a(n, k, l):
    bits = itertools.combinations(range(1,n+1), k)
    #  prod = lambda bit: reduce(lambda x, y: x * y, bit) if len(bit) > 0 else 1
    prod = lambda bit: reduce(lambda x, y: x * y, bit) if len(bit) > 0 else 1
    mid = k/2
    it = 0
    l = [[1]*(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))]  # all the combinations
    for bit in bits:
        p1 = prod(bit[0:mid])
        p2 = prod(bit[mid:])
        break
    l[0][0] = p1*p2
    for bit in bits:
        it +=1
        l[0][it] = p1*prod(bit[mid:]) if it< mid else prod(bit)
    return l


def kbits3b(n, k, l):
    if k == 1:
        return range(1,n+1)
    bits = itertools.combinations(range(1,n+1), k)
    #  prod = lambda bit: reduce(lambda x, y: x * y, bit) if len(bit) > 0 else 1
    prod = lambda bit: reduce(lambda x, y: x * y, bit)
    mid = max(k/2,n/2)
    it = 0
    N = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    l = [1] * N  # all the combinations
    for bit in bits:
        p1 = prod(bit[0:mid])
        p2 = prod(bit[mid:])
        checkpoint = bit[0:mid]
        break
    l[0] = p1*p2
    for bit in bits:
        it += 1
        if not bit[0:mid] == checkpoint:
            checkpoint = bit[0:mid]
            p1 = prod(bit[0:mid])
        l[it] = p1 * prod(bit[mid:])
    return l


def kbits3c(n, k, l): # bad
    if k == 1:
        return range(1,n+1)

    bits = itertools.combinations(range(1, n + 1), k)  # all the combinations
    prod = lambda bit: reduce(lambda x, y: x * y, bit)  # [1,2,3] => 1*2*3
    N = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))  # combinations
    l = [1] * N  # pre allocate space for the results
    r = [0] + range(2, k - 1, 6) + [k]
    p = ['None'] * (len(r) - 1)
    for bit in bits:
        for i in range(0, len(r) - 1):
            p[i] = prod(bit[r[i]:r[i + 1]])
        break

    bits = itertools.combinations(range(1, n + 1), k)  # all the combinations
    for bit in bits:
        print bit

    l[0] = prod(p)
    it = 0
    for bit in bits:
        it += 1
        change_point = (k - it % k) % k # the changing posstion is too difficult to aquire and is not only one
        i = sum(map(lambda x: x <= change_point, r)) - 1
        p[i] = prod(bit[r[i]:r[i + 1]])
        l[it] = prod(p)
        print "~~~~"
        print "bit:" + str(list(bit))
        print "it:" + str(it)
        print "k:" + str(k)
        print "r:" + str(r)
        print "p:" + str(p)
        print "l[it]:" + str(l[it])

        return l


def kbits3f(n, k, l): #best
    if k == 1:
        return range(1, n + 1)

    bits = itertools.combinations(range(1, n + 1), k)  # all the combinations
    prod = lambda bit: reduce(lambda x, y: x * y, bit)  # [1,2,3] => 1*2*3

    if k < 3:
        return map(prod, bits)

    N = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))  # combinations
    l = [1] * N  # pre allocate space for the results
    stable_point = k-1
    stable_value = -1

    for bit in bits:
        p1 = prod(bit[0:stable_point])
        stable_value = bit[stable_point]
        p2 = prod(bit[stable_point:])
        break

    l[0] = p1 * p2
    it = 0
    for bit in bits:
        it += 1
        # print "bit : " + str(bit)
        if stable_value != bit[stable_point]:
            if stable_point > 1:
                stable_point -= 1
                p1 = prod(bit[0:stable_point])
                stable_value = bit[stable_point]
                # print "c1:: point:" + str(stable_point) + " - value:" + str(stable_value) + " - p1:" + str(p1)
            else:
                stable_point = 0
                p1 = 1
                stable_value = bit[stable_point]
                # print "c2:: point:" + str(stable_point)  + " - value:" + str(stable_value) + " - p1:" + str(p1)
        p2 = prod(bit[stable_point:])
        l[it] = p1*p2
        # print "it: " + str(l[it])
    return l


def kbits3d(n,k,l):
    if k == 1:
        return range(1,n+1)
    bits = itertools.combinations(range(1,n+1), k)
    #  prod = lambda bit: reduce(lambda x, y: x * y, bit) if len(bit) > 0 else 1
    prod = lambda bit: reduce(lambda x, y: x * y, bit)
    mid = max(k/2, n - 20)
    it = 0
    N = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    l = [1] * N  # all the combinations
    for bit in bits:
        p1 = prod(bit[0:mid])
        p2 = prod(bit[mid:])
        checkpoint = bit[0:mid]
        break
    l[0] = p1*p2
    for bit in bits:
        it += 1
        if not bit[0:mid] == checkpoint:
            checkpoint = bit[0:mid]
            p1 = prod(bit[0:mid])
        l[it] = p1 * prod(bit[mid:])
    return l

# timeit.timeit('kbits3b(63, 59, 1)', setup="from __main__ import kbits3b", number=1)

'''
n=63;
k=59
l = kbits2(n,k,1)
m = kbits3c(n,k,1)
i = 0
while l[i:(i+10)]==m[i:(i+10)]:
    i+=1

bits = itertools.combinations(range(1,n+1), k)
j=0
for bit in bits:
    j+=1
    if math.fabs(i-j)<3:
        print bit
    if j - i > 3:
        break

n=8;k=5;
bits = itertools.combinations(range(1,n+1), k)
for bit in bits:
    print bit
'''

def kbits_cashed(n, k, l):
    bits = itertools.combinations(range(1, n + 1), k)
    return map(lambda bit: reduce(lambda x, y: get(x, y), bit), bits)


def get(x, y):
    # note: the values are sorted x<y
    key = "%d,%d" % (x, y)
    try:
        return mult[key]
    except Exception:
        mu = x * y
        mult[key] = mu
        return mu

class MyList(MutableSequence):
    def __init__(self, type, iterable=()):
        self._data = []
        self._type = type
        self.extend(iterable)

    def insert(self, index, item):
        # if not isinstance(item, self._type):
        #    raise TypeError
        self._data.insert(index, item)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, *args):
        return self._data.__getitem__(*args)

    def __delitem__(self, *args):
        self._data.__delitem__(*args)

    def __setitem__(self, key, value):
        self._data[k] = value
# timeit.timeit('kbits(19, 18, 1)', setup="from __main__ import kbits", number=10)
# timeit.timeit('kbits2(19, 18, 1)', setup="from __main__ import kbits2", number=10)