from sys import stdin

grid = {}
row = -1
trailheads = []
for line in stdin:
    line = [int(l) for l in line.strip()]
    row += 1
    for col, val in enumerate(line):
        grid[(row, col)] = val
        if val == 0:
            trailheads.append((row, col))

def step(path, start):
    if grid[start] == 9:
        return [start]
    r, c = start
    response = []
    for next in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
        if next not in grid:
            continue
        if next in path:
            continue
        if grid[next] == grid[start]+1:
            response += step(path + [start], next)
    return response

total = 0
for trailhead in trailheads:
    total += len(step([], trailhead))
print(total)