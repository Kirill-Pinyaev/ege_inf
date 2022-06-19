def f(a):
    s = a
    s //= 15
    n = 14
    while s < 285:
        if (s + n) % 9 == 0:
            s += 11
        n += 13
    return n


sp = []
for i in range(100000):
    if f(i) == 118:
        sp.append(i)
print(len(sp))