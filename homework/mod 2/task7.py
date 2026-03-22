text = input()
parts = text.split(',')

s = parts[0]
i = parts[1]

count = 0

for a in s:
    if a == i:
        count = count + 1
    else:
        break

print(count)