x = input()

zeros = 0
ones = 0

for a in x:
    if a == '0':
        zeros = zeros + 1
    if a == '1':
        ones = ones + 1

if zeros == ones:
    print("yes")
else:
    print("no")