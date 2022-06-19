def f(a):
    s = a
    p = 13
    q = 4
    k1 = 0
    k2 = 0
    while s != 1280:
        s += p
        k1 += 1
        if s > 1280:
            return 0, 0
    while s != q + k1:
        s -= q
        k2 += 1
        if s < (q + k1):
            return 0, 0
    k1 += s
    k2 += s
    return k1, k2


sp = []
for i in range(100000):
    a, b = f(i)
    if a == 36 and b == 335:
        sp.append(i)
print(sp)