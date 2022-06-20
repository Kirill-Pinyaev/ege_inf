for a in range(500):
    ok = True
    for x in range(500):
        for y in range(500):
            ok *= (((2 * y + x) != 70) or (x < y) or (a < x))
            if not ok:
                continue
        if not ok:
            break
    if ok:
        print(a)