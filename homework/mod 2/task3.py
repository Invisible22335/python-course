s = input()

parts = s.split()

a = int(parts[0])
b = int(parts[1])
c = int(parts[2])

if (a <= b <= c) or (c <= b <= a):
    print(b)
elif (b <= a <= c) or (c <= a <= b):
    print(a)
else:
    print(c)