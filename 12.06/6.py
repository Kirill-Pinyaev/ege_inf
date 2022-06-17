def f(a):
    s = a
    s //= 3
    n = 0
    while s < 335:
        s += 9
        n += 5
    return n


sp = []
for i in range(10000):
    if f(i) > 0:
        sp.append(f(i))
sp = set(sp)
sp = list(sp)
print(len(sp))