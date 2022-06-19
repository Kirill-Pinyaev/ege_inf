def f(a):
    s = a
    s = (s + 31) // 26
    n = 813
    while s > 0:
        n //= 3
        s -= n
    return n


sp = []
for i in range(10000):
    if f(i) == 30:
        sp.append(i)
print(sp)