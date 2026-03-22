def f(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    m = ''
    l = ''
    for k in d:
        if d[k] % 2 == 1:
            if m != '':
                return 'Нельзя составить палиндром'
            m = k
        l += k * (d[k] // 2)
    return l + m + l[::-1]

print(f(input()))