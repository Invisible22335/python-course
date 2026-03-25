n = int(input("Введите количество имен: "))

names = []
for i in range(n):
    name = input("Введите имя: ")
    names.append(name)

uni = []

for name in names:
    found = False
    for u in uni:
        if len(name) == len(u):
            found = True
            break
    if not found:
        uni.append(name)

print("Исходный список:", names)
print("Список uni:", uni)