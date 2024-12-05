row = 0
col = 0

'''
rise_mod = range(0, 4)
no_mod = [0, 0, 0, 0]
down_mod = range(-3, 0)

mods = [rise_mod, no_mod, down_mod]
for mod in mods:
'''

'''
def vector(row, rmod, col, cmod):
    coords = []
    for delta in range(0, 4):
        coords.append((row + (rmod * delta), col + (cmod * delta)))
    return coords

def target(row, col):
    targets = []
    for rmod in range(-1, 2):
        for cmod in range(-1, 2):
            yield vector(row, rmod, col, cmod)

    return coords
'''

def target(row, col):
    for rmod in range(-1, 2):
        for cmod in range(-1, 2):
            if rmod == 0 and cmod == 0:
                continue
            coords = []
            for delta in range(0, 4):
                coords.append((row + (rmod * delta), col + (cmod * delta)))
            yield coords

grid = []
r = list(" " * 7)
for i in range(7):
    grid.append(r.copy())

for t in target(3, 3):
    print()
    print(t)
    g = grid.copy()
    for coord in t:
        ro, co = coord
        g[ro][co] = "X"
    for row in grid:
        print(row)