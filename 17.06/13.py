for a in range(1, 500):
    ok = True
    for x in range(1, 500):
        ok *= (((x & 107) == 0) <= (((x & 55) != 0) <= ((x & a) != 0)))
        if not ok:
            break
    if ok:
        print(a)