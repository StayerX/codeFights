import itertools, math, decimal

mult = {}

def first_kind_sum_it_up(n, k):
    r = kbits(n,k,1)
    div = max(r)*1.0
    res = sum([div/x for x in r])/div
    d = decimal.Decimal(res).as_tuple()
    pow = len(d.digits) + d.exponent - 1
    re = "%.2f" % round(res*math.pow(10,-pow),2)
    res = ('%sE+%d' % (re,pow)) if pow>=0 else ('%sE%d' % (re,pow))
    return res

def kbits(n, k, l):
    bits = itertools.combinations(range(1,n+1), k)
    # bits = itertools.islice(bits,l)
    return map(lambda bit: reduce(lambda x,y: get(x,y), bit),bits)

def get(x,y):
    #note: the values are sorted x<y
    key = "%d,%d" % (x,y)
    try:
        return mult[key]
    except Exception:
        mu = x*y
        mult[key] = mu
        return mu