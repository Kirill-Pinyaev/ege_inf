def f(n):
    b = bin(n)[2:]
    b += b[-2]
    b += b[1]
    return int(b, 2)


sp = []
for i in range(2, 1000):
    if f(i) > 170:
        sp.append(i)
print(sp)