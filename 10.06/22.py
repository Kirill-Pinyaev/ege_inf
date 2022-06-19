def f(a):
    p = a
    q = 11
    k = 0
    while p >= q:
        k += 3
        p -= q
    n = p
    if n < k:
        n = k
        k = p
    return k, n


sp = []
for i in range(41, 1000):
    a, b = f(i)
    if (a + b) % 17 == 0:
        sp.append(i)
print(sp)