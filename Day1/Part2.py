# Think I'll go with `cat file.txt | python script.py` this year
from sys import stdin
raw = [line.rstrip() for line in stdin]

first = []
modifier = {}
for line in raw:
    l, r = [int(i) for i in line.split()]
    first.append(l)
    if r not in modifier:
        modifier[r] = 1
    else:
        modifier[r] += 1
    if l not in modifier:
        modifier[l] = 0
answer = sum([f * modifier[f] for f in first])
print(answer)