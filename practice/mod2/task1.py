import re

line = input("Введите текст: ")

regex = r'\b20\d{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01]) (?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d\b'

found_dates = re.findall(regex, line)

for d in found_dates:
    print(d)