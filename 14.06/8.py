s = '8' * 295
while '22' in s or '88' in s:
    if '22' in s:
        s = s.replace('22', '888', 1)
    else:
        s = s.replace('88', '2', 1)
print(s)