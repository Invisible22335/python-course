def f(a):
    if len(set(a)) == 1:
        return 'Все числа равны'
    if len(set(a)) == len(a):
        return 'Все числа разные'
    return 'Есть равные и неравные числа'

print(f(input().split()))