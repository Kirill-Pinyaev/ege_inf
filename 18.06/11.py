for a in range(1, 500):
    ok = True
    for x in range(500):
        for y in range(500):
            ok *= ((((2 * x) + (3 * y)) != 72) or ((a > x) and (a > y)))
            if not ok:
                continue
        if not ok:
            break
    if ok:
        print(a)