with open('26_120622.txt') as f:
    sp_z = []
    sp_q = []
    n, m = 10000, 100000
    for i in f:
        s = i.split()
        if s[1] =='Z':
            sp_z.append(((int(s[0])), s[1]))
        else:
            sp_q.append(((int(s[0])), s[1]))
    sp_q = sorted(sp_q)
    sp_z = sorted(sp_z)
    sp = []
    for i in range(n):
        if sp_z != [] and sp_q != []:
            if m - sp_z[0][0] >= 0 or m - sp_q[0][0] >= 0:
                if sp_z[0][0] < sp_q[0][0]:
                    sp.append(sp_z[0])
                    m -= sp_z[0][0]
                    a = sp_z.pop(0)
                else:
                    sp.append(sp_q[0])
                    m -= sp_q[0][0]
                    a = sp_q.pop(0)
    count = 0
    for i in sp:
        if i[1] == 'Z':
            count += 1
    print(len(sp))
    print(count)
    print(m)
