phrases = input("Введите фразы через ; : ").split(";")
lengths = [len(phrase.split()) for phrase in phrases]

print("Исходный список:", phrases)
print("Список lengths:", lengths)