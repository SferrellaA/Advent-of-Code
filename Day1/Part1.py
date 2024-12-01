from sys import argv
try:
    raw = open(argv[1]).read()
except:
    print("Couldn't open file")
    exit()

left = []
right = []
for line in raw.split("\n"):
    if line == "":
        continue
    l, r = [int(n) for n in line.split()]
    left.append(l)
    right.append(r)
left.sort()
right.sort()

answer = sum([abs(l-r) for l, r in zip(left, right)])
print(answer)