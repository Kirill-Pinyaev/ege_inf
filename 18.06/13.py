for a in range(1, 500):
    ok = True
    for x in range(1, 500):
        ok *= (((x & 102) != 0) <= (((x & 36) == 0) <= ((x & a) != 0)))
        if not ok:
            continue
    if ok:
        print(a)