from sys import stdin

grid = {}
row = -1
centers = []
for line in stdin:
    row += 1
    for column, letter in enumerate([c for c in line.strip("\n")]):
        grid[(row, column)] = letter
        if letter == "A":
            centers.append((row, column))

def check(row, col):
    try:
        zig = [grid[(row-1,col-1)], grid[(row+1,col+1)]]
        zag = [grid[(row-1,col+1)], grid[(row+1,col-1)]]
    except:
        return False
    if "M" in zig and "M" in zag:
        if "S" in zig and "S" in zag:
            return True
    return False

count = 0
for coord in centers:
    if check(*coord):
        count += 1
print(count)