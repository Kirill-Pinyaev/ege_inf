def f(a):
    s = a
    s //= 2
    n = 0
    while s < 235:
        s += 7
        n += 3
    return n


sp = []
for i in range(1000):
    if f(i) == 12:
        sp.append(i)
print(sp)