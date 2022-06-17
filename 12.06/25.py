#1000000000
#1**234?91
sp = []
for i in range(10):
    a = int(f'1234{i}91')
    if a % 133 == 0:
        sp.append((a, a // 133))
for j in range(10):
    for i in range(10):
        a = int(f'1{j}234{i}91')
        if a % 133 == 0:
            sp.append((a, a // 133))
for k in range(10):
    for j in range(10):
        for i in range(10):
            a = int(f'1{k}{j}234{i}91')
            if a % 133 == 0:
                sp.append((a, a // 133))
for i in sp:
    print(*i)