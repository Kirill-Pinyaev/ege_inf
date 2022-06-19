def f(a):
    x = a
    l = 0
    m = 0
    while x > 0:
        l += 1
        if x % 2 == 0:
            m += (x % 10) // 2
        x //= 10
    return l, m


sp = []
for i in range(1000):
    a, b = f(i)
    if a == 3 and b == 7:
        sp.append(i)
print(sp)