with open('26_1.txt') as f:
    n, k = list(map(int, f.readline().split()))
    sp = list(map(int, f.readlines()))
    sp = sorted(sp)
    data = []
    for i in range(n):
        a = sp[i]
        count = 1
        for j in range(i + 1, n):
            if sp[j] - a >= 3:
                a = sp[j]
                count += 1
        data.append((count, sp[i]))
    data = sorted(data, key=lambda x: (-x[0], -x[1]))
    print(*data[0])