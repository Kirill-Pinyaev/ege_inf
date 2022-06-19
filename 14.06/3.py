def f(n):
    b = bin(n)[2:]
    b += str(b.count('1') % 2)
    b += str(b.count('1') % 2)
    return int(b, 2)


sp = []
for i in range(1000):
    a = f(i)
    if a > 145:
        sp.append(a)
print(sp)
