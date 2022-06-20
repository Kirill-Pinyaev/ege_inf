#1000000000
#123**567?
sp = []
for i in range(10):
    a = int(f'123567{i}')
    if a % 169 == 0:
        sp.append((a, a // 169))
for k in range(10):
    for i in range(10):
        a = int(f'123{k}567{i}')
        if a % 169 == 0:
            sp.append((a, a // 169))
for j in range(10):
    for k in range(10):
        for i in range(10):
            a = int(f'123{j}{k}567{i}')
            if a % 169 == 0:
                sp.append((a, a // 169))
sp = sorted(sp)
for i in sp:
    print(*i)
