import re

data = input("Введите текст: ")

mail_pattern = r'[A-Za-z0-9+_#-]+@[A-Za-z0-9+_#-]+\.[A-Za-z]+'

mail_list = re.findall(mail_pattern, data)

for m in mail_list:
    print(m)