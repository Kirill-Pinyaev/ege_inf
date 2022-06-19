with open('26_180622.txt') as f:
    data = []
    for i in f:
        data.append(list(map(int, i.split())))
    n, m = data.pop(0)
    data = sorted(data, key=lambda x: x[0] -x[1])
    sp = [[]]
    a = data[0][1]
    count = 0
    for i in range(n):
        if data[i][1] == a:
            sp[count].append(data[i])
        if data[i][1] != a:
            sp.append([])
            count += 1
            a = data[i][1]
    sp2 = []
    for i in sp:
        lst = []
        for j in i:
            lst.append(j[2])
        if len(lst) <= 2:
            if len(lst) == 1:
                if lst[0] == 1 or lst[0] == 6:
                    sp2.append(i)
            if len(lst) == 2:
                lst = sorted(lst)
                if lst[0] == 1 and lst[1] == 6:
                    sp2.append(i)
    print(sp2)
    print(len(sp2))
