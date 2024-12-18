from sys import stdin

# I should probably make a helper function for this by now
def adjacent(coord):
    row, col = coord
    yield (row-1, col)
    yield (row, col-1)
    yield (row+1, col)
    yield (row, col+1)

grid = {}
row = 0
for line in stdin:
    row += 1
    col = 0
    for crop in list(line.strip()):
        col += 1
        if crop not in grid:
            grid[crop] = []
        grid[crop].append((row, col))

def seek(crop, path, start):
    if start in path:
        return
    global grid
    if start not in grid[crop]:
        return
    path.append(start)
    grid[crop].remove(start)
    for neighbor in adjacent(start):
        seek(crop, path, neighbor)

'''
A region of R plants with price 12 * 18 = 216.
A region of I plants with price 4 * 8 = 32.
A region of C plants with price 14 * 28 = 392.
A region of F plants with price 10 * 18 = 180.
A region of V plants with price 13 * 20 = 260.
A region of J plants with price 11 * 20 = 220.
A region of C plants with price 1 * 4 = 4.
A region of E plants with price 13 * 18 = 234.
A region of I plants with price 14 * 22 = 308.
A region of M plants with price 5 * 12 = 60.
A region of S plants with price 3 * 8 = 24.
'''

total = 0
for crop in grid:
    while len(grid[crop]) > 0:
        field = []
        seek(crop, field, grid[crop][0])
        perimeter = 0
        for plot in field:
            perimeter += 4
            for neighbor in adjacent(plot):
                if neighbor in field:
                    perimeter -= 1
        total += (len(field) * perimeter)
print(total)