a = input()

parts = a.split(".")

i = len(parts) - 1
while i >= 0:
    print(parts[i])
    i = i - 1