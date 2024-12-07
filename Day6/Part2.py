# Sample has 6 spots
from sys import setrecursionlimit
setrecursionlimit(10**7) # don't judge me

from grid import read_stdin
grid, guard = read_stdin("^")
grid[guard] = "."

def scan(row, col, face, path, start):
    if (row, col) not in grid:
        #print(path)
        return False
    if len(path) > 0 and (row, col) == start:
        return True
    if grid[(row, col)] == "#":
        return "#"
    if (row, col, face) in path:
        return True
    path.append((row, col, face))
    report = None
    if face == "^":
        report = scan(row-1, col, face, path, start)
        if report == "#":
            report = scan(row, col+1, ">", path, start)
    if face == ">":
        report = scan(row, col+1, face, path, start)
        if report == "#":
            report = scan(row+1, col, "v", path, start)
    if face == "v":
        report = scan(row+1, col, face, path, start)
        if report == "#":
            report = scan(row, col-1, "<", path, start)
    if face == "<":
        report = scan(row, col-1, face, path, start)
        if report == "#":
            report = scan(row-1, col, "^", path, start)
    if report == "#":
        # what?
        return False
    return report

potentials = []

def step(row, col, face):
    if (row, col) not in grid:
        return "done"
    rotate = False
    report = None
    if grid[(row, col)] == "#":
        rotate = True
    if face == "^":
        if rotate:
            return (row+1, col+1, ">")
        if scan(row, col, ">", [], (row, col)):
            potentials.append((row, col, face))
        return (row-1, col, face)
    if face == ">":
        if rotate:
            return (row+1, col-1, "v")
        if scan(row, col, "v", [], (row, col)):
            potentials.append((row, col, face))
        return (row, col+1, face)
    if face == "v":
        if rotate:
            return (row-1, col-1, "<")
        if scan(row, col, "<", [], (row, col)):
            potentials.append((row, col, face))
        return (row+1, col, face)
    if face == "<":
        if rotate:
            return (row-1, col+1, "^")
        if scan(row, col, "^", [], (row, col)):
            potentials.append((row, col, face))
        return (row, col-1, face)

row, col = guard
face = "^"
while True:
    #print(row, col, face)
    report = step(row, col, face)
    if report == "done":
        break
    row, col, face = report

print(potentials)
print(len(potentials))

# 1835 is too high, 1746 too low
