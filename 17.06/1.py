print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not(((w <= y) and ((not x) <= z)) <= ((z == w) or (y and (not x)))):
                    print(w, x, y, z)