s = 'АИОУЭ'
sp = []
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for j in s:
                        sp.append(a + b + c + d + e + j)
print(sp.index('ОЭЭЭЭО') + 1)