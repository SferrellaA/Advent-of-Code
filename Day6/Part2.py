# Sample has 6 spots
from sys import setrecursionlimit
setrecursionlimit(10**7) # don't judge me

from grid import read_stdin
grid, guard = read_stdin("^")
grid[guard] = "."

def ahead(row, col, face):
    if face == "^":
        return (row-1, col)
    if face == ">":
        return (row, col+1)
    if face == "v":
        return (row+1, col)
    if face == "<":
        return (row, col-1)

def rotate(face):
    if face == ">":
        return "v"
    if face == "v":
        return "<"
    if face == "<":
        return "^"
    if face == "^":
        return ">"

'''
def step(row, col, face):
    facing = ahead(row, col, face)
    if facing not in grid:
        return True, None
    if grid[facing] == "#":
        face = rotate(face)
    else:
        row, col = facing
    return False, (row, col, face)
'''

def scan(row, col, face):
    potential = ahead(row, col, face)
    path = []
    while True:
        if (row, col, face) in path:
            return True
        path.append((row, col, face))

        facing = ahead(row, col, face)
        if facing not in grid:
            return False
        if grid[facing] == "#" or facing == potential:
            face = rotate(face)
        else:
            row, col = facing


row, col = guard
face = "^"
blockers = []

while True:
    facing = ahead(row, col, face)
    if facing not in grid:
        break

    if scan(row, col, face):

        blockers.append(ahead(row, col, face))
    
    if grid[facing] == "#":
        face = rotate(face)
    else:
        row, col = facing

print(blockers)
print(len(blockers))       
# 1835 is too high, 1746 too low




'''
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
'''

