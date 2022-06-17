def f(n, m):
    if n % m == 0:
        return 1
    return 0


for a in range(1, 500):
    ok = True
    for x in range(1, 500):
        ok *= ((f(x, 12) <= (not f(x, 90))) or ((x + 2 * a) >=512))
        if not ok:
            continue
    if ok:
        print(a)