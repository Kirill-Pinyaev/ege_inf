def f(n):
    b = bin(n)[2:]
    b += str(b.count('1') % 2)
    if int(b) % 2 == 0:
        b += '1'
    return int(b, 2)



sp = []
for i in range(1000):
    if f(i) > 225:
        sp.append(i)
print(sp)