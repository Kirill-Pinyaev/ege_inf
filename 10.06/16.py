def f(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + 1 + f(n - 1)
    elif n % 2 != 0 and n > 1:
        return 4 * f(n - 2)

print(f(22))