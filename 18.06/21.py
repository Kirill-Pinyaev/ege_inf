#10000000000
#1?2139***4
sp = []
for i in range(10):
    a = int(f'1{i}21394')
    if a % 2022 == 0:
        sp.append((a, a // 2022))
for j in range(10):
    for i in range(10):
        a = int(f'1{i}2139{j}4')
        if a % 2022 == 0:
            sp.append((a, a // 2022))
for k in range(10):
    for j in range(10):
        for i in range(10):
            a = int(f'1{i}2139{k}{j}4')
            if a % 2022 == 0:
                sp.append((a, a // 2022))
for l in range(10):
    for k in range(10):
        for j in range(10):
            for i in range(10):
                a = int(f'1{i}2139{l}{k}{j}4')
                if a % 2022 == 0:
                    sp.append((a, a // 2022))
sp = sorted(sp)
for i in sp:
    print(*i)
