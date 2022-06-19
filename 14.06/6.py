def f(n, m):
    if n % m == 0:
        return 1
    return 0


for a in range(1, 500):
    ok = True
    for x in range(1, 500):
        ok *= ((not(f(x, a) and f(x, 15))) <= (not(f(x, 18)) or (not(f(x, 15)))))
        if not ok:
            continue
    if ok:
        print(a)