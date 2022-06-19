#10000000000
#9297134511
#?2***345?1
sp = []
for i in range(1, 10):
    for j in range(10):
        a = int(f'{i}2345{j}1')
        if a % 9709 == 0:
            sp.append((a, a // 9709))
for k in range(10):
    for i in range(1, 10):
        for j in range(10):
            a = int(f'{i}2{k}345{j}1')
            if a % 9709 == 0:
                sp.append((a, a // 9709))
for l in range(10):
    for k in range(10):
        for i in range(1, 10):
            for j in range(10):
                a = int(f'{i}2{l}{k}345{j}1')
                if a % 9709 == 0:
                    sp.append((a, a // 9709))
for h in range(10):
    for l in range(10):
        for k in range(10):
            for i in range(1, 10):
                for j in range(10):
                    a = int(f'{i}2{h}{l}{k}345{j}1')
                    if a % 9709 == 0:
                        sp.append((a, a // 9709))
sp = sorted(sp, reverse=True)
for i in sp:
    print(*i)