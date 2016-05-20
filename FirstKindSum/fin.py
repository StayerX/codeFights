import itertools, math, decimal
d = {}

def first_kind_sum_it_up(n, k):
    r = C(n+1,k+1)
    d = math.factorial(n)*1.0
    res = r/d
    d = decimal.Decimal(res).as_tuple()
    pow = len(d.digits) + d.exponent - 1
    re = "%.2f" % round(res*math.pow(10,-pow),2)
    res = ('%sE+%d' % (re,pow)) if pow>=0 else ('%sE%d' % (re,pow))
    return res

def C(n,k):
    if (n,k) in d: return d[n,k]
    o = n-1
    l = k-1
    if n == 0 and k == 0:
        r = 1
    elif n < 1 or k < 1:
        r = 0
    else:
        r = o * C(o, k) + C(o, l)
    d[n, k] = r
    return r


'''
# <editor-fold desc="Description">
import decimal
c={}
def S(n, k):
    t = n - 1
    if (n, k) in c: return c[n, k]
    else:
        if n == 0 and k == 0: r = 1
        elif n < 1 or k < 1: r = 0
        else: r = t * S(t, k) + S(t, k - 1)
        c[n, k] = r
        return r
First_Kind_Sum_It_Up = lambda n, k: "{:.2E}".format(decimal.Decimal(S(n + 1,k + 1)) / math.factorial(n))
# </editor-fold>
'''
