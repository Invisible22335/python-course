s = input()

result = ""

for i in s:
    if i >= '0' and i <= '9':
        result = result + i
    elif i == '+':
        result = result + i

print(result)