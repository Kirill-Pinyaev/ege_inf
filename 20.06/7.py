def f(n, m):
    if n % m == 0:
        return 1
    return 0


for a in range(1, 500):
    ok = True
    for x in range(1, 500):
        ok *= ((f(x, 250) <= (not f(x, 10))) or ((3 * x + 2 * a) >= 1000))
        if not ok:
            break
    if ok:
        print(a)