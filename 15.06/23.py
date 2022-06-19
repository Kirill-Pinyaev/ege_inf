def f(n):
    if n == 512:
        return 1
    elif n > 512:
        return 0
    else:
        return f(int('1' + str(n))) + f(n + 1)
print(f(1))
