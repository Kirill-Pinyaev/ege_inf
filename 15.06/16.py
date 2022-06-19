def f(n):
    if n < 2:
        return 1
    elif n % 2 == 0:
        return f(n // 2) + 1
    else:
        return f(n - 3) + 3

sp = []
for i in range(10000):
    if f(i) == 31:
        sp.append(i)
print(sp)