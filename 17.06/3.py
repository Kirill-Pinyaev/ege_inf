def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b += bin(b.count('1'))[2:]
    else:
        b = '1' + b + '00'
    return int(b, 2)


sp = []
for i in range(10000):
    if 500 <= f(i) <= 700:
        sp.append(i)
print(len(sp))