#10000000000
#3?87**6?21
sp = []
for i in range(10):
    for j in range(10):
        a = int(f'3{i}876{j}21')
        if a % 1597 == 0:
            sp.append((a, a // 1597))
for k in range(10):
    for i in range(10):
        for j in range(10):
            a = int(f'3{i}87{k}6{j}21')
            if a % 1597 == 0:
                sp.append((a, a // 1597))
for l in range(10):
    for k in range(10):
        for i in range(10):
            for j in range(10):
                a = int(f'3{i}87{l}{k}6{j}21')
                if a % 1597 == 0:
                    sp.append((a, a // 1597))
sp = sorted(sp)
for i in sp:
    print(*i)