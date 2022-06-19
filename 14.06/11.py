def f(a):
    x = a
    q = 11
    l = 0
    while x >= q:
        l += 1
        x -= q
    m = x
    if m < l:
        m = l
        l = x
    return l, m


sp = []
for i in range(11, 10000):
    a, b = f(i)
    if a == 7 and b == 8:
        sp.append(i)
print(sp)