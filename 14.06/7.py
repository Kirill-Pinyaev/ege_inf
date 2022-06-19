def f(n, m):
    if n % m == 0:
        return 1
    return 0


for a in range(1, 500):
    ok = True
    for x in range(1, 500):
        ok *= ((f(x, 3) <= (not(f(x, 5)))) or ((x + a) >= 70))
        if not ok:
            continue
    if ok:
        print(a)