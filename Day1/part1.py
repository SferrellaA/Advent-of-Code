from sys import argv
total = 0
for line in open(argv[1]).readlines():
    num = ''
    for c in line:
        if (c.isdigit()):
            num = c
            break
    for c in line[::-1]:
        if (c.isdigit()):
            num += c
            break
    total += int(num)
print(total)