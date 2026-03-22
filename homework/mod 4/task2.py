def f(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return f(a * a, n // 2)
    return a * f(a, n - 1)

a, n = map(int, input().split())
print(f(a, n))