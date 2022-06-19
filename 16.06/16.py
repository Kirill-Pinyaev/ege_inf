def s(a):
    a = str(a)
    summ = 0
    for i in a:
        summ += int(i)
    return summ


def f(n):
    if n < 3:
        return 1
    elif s(n) % 2 == 0:
        return f(n - 1) - f(n - 2)
    else:
        return f(n - 1) + f(n // 2)
print(f(100))