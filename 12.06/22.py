def f(a):
    d = a
    c = 0
    n = 0
    t = d
    while n != 144:
        n += t
        t += d
        c += 1
        if n > 144:
            return 0
    if c % 2 != 0:
        c += 5
    return c


sp = []
for i in range(1, 10000):
    if f(i) == 8:
        sp.append(i)
print(sp)