def f(a, b):
    if b == 0:
        return a
    return f(b, a % b)

a, b = map(int, input().split())
print(f(a, b))