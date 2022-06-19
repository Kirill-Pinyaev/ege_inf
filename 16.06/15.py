for a in range(500):
    ok = True
    for x in range(500):
        for y in range(500):
            ok *= ((75 != (y + 2 * x)) or (a < x) or (a < y))
            if not ok:
                continue
        if not ok:
            break
    if ok:
        print(a)