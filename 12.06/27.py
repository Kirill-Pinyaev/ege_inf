with open('27_test.txt') as f:
    data = list(map(int, f.readlines()))
    n = 4
    sp = []
    for i in range(n):
        for j in range(i +1, n +1):
            sp.append(data[i:j])
    sp2 = []
    print(sp)
    for i in sp:
        if sum(i) % 12 == 0:
            sp2.append(i)
    print(len(sp2))