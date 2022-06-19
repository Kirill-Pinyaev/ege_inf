s = '7' * 91
while '7777' in s or '3333' in s:
    if '7777' in s:
        s = s.replace('7777', '3', 1)
    else:
        s = s.replace('3333', '77', 1)
print(s)