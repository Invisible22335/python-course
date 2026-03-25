n = int(input("Введите число N: "))

numbers = list(range(n, n**2 + 1))
roots = [x ** 0.5 for x in numbers]

print("Список чисел:", numbers)
print("Список корней:", roots)