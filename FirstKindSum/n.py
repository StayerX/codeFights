#S = lambda n,k : n == k or n > 0 and k > 0 and ~-n*S(n - 1, k) + S(n - 1, k - 1)
def First_Kind_Sum_It_Up(n, k):
u = n + 2
m = [1] + [0]*u**2
c = j = 0
while j < k + 1:
    j += 1
    i = j
    while i < u:
        t = j*u + i
        x = m[t] = ~-i*m[t - 1] + m[t - n - 3]
        i += 1
while n:
    x /= n
    n -= x > 9e9 or 1.
    while x < 1:
        c += 1
        x *= 10
return "%.2fE"%x+"+-"[c>0::2]+`c`