#10000000
#14?4***
def f(n):
    lst = []
    for i in range(2, n):
        if n % i == 0 and i % 2 != 0:
            lst.append(i)
    return sum(lst)
sp = []
for i in range(10):
    a = int(f'14{i}4')
    if a % 217 == 0:
        sp.append((a, f(a)))
for j in range(10):
    for i in range(10):
        a = int(f'14{i}4{j}')
        if a % 217 == 0:
            sp.append((a, f(a)))
for k in range(10):
    for j in range(10):
        for i in range(10):
            a = int(f'14{i}4{k}{j}')
            if a % 217 == 0:
                sp.append((a, f(a)))
for l in range(10):
    for k in range(10):
        for j in range(10):
            for i in range(10):
                a = int(f'14{i}4{l}{k}{j}')
                if a % 217 == 0:
                    sp.append((a, f(a)))
sp = sorted(sp, reverse=True)
sp = sp[:7]
for i in sp:
    print(*i)