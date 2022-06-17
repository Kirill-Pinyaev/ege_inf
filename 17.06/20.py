#10000000000
#12***714?5
sp = []
for i in range(10):
    a = int(f'12714{i}5')
    if a % 2003 == 0:
        sp.append((a, a // 2003))
for j in range(10):
    for i in range(10):
        a = int(f'12{j}714{i}5')
        if a % 2003 == 0:
            sp.append((a, a // 2003))
for k in range(10):
    for j in range(10):
        for i in range(10):
            a = int(f'12{k}{j}714{i}5')
            if a % 2003 == 0:
                sp.append((a, a // 2003))
for l in range(10):
    for k in range(10):
        for j in range(10):
            for i in range(10):
                a = int(f'12{l}{k}{j}714{i}5')
                if a % 2003 == 0:
                    sp.append((a, a // 2003))
sp = sorted(sp)
for i in sp:
    print(*i)