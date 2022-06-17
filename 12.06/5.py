def f(n):
    b = bin(n)[2:]
    b += str(b.count('1') % 2)
    b += str(b.count('1') % 2)
    return int(b, 2)


sp = []
for i in range(1000):
    if f(i) > 137:
        sp.append(i)
print(sp)