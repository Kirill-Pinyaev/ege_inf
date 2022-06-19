#1000000000
#23**45?67
sp = []
for i in range(10):
    a = int(f'2345{i}67')
    if a % 217 == 0:
        sp.append((a, a // 217))
for j in range(10):
    for i in range(10):
        a = int(f'23{j}45{i}67')
        if a % 217 == 0:
            sp.append((a, a // 217))
for k in range(10):
    for j in range(10):
        for i in range(10):
            a = int(f'23{k}{j}45{i}67')
            if a % 217 == 0:
                sp.append((a, a // 217))
for i in sp:
    print(*i)