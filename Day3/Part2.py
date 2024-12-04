from sys import stdin
import re
raw = "do()" + "".join([line for line in stdin])

filtered = ""
for piece in raw.split("don't()"):
    subpiece = piece.split("do()")
    if len(subpiece) > 1:
        filtered += "".join(subpiece[1:])

def handle_match(command):
    a, b = command[4:-1].split(',')
    a = int(a)
    b = int(b)
    if a > 1000 or b > 1000: # simpler than doing regex
        return 0 # don't need a special handler :p
    return a * b

running_total = 0
for match in re.findall(r'(mul\(\d+?,\d+?\))', filtered):
    running_total += handle_match(match)
print(running_total)