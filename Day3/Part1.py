from sys import stdin
from re import findall

lines = [line.strip("\n") for line in stdin]

def handle_match(command):
    a, b = command[4:-1].split(',')
    a = int(a)
    b = int(b)
    if a > 1000 or b > 1000: # simpler than doing regex
        return 0 # don't need a special handler :p
    return a * b

running_total = 0
for line in lines:
    for match in findall(r'mul\(\d+,\d+\)', line):
        running_total += handle_match(match)
print(running_total)