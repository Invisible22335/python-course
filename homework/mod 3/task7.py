s = input()
print("".join([c for c in s if c.isdigit() or c == '+']))