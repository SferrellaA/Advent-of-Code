# Sample has 41 spots
from sys import setrecursionlimit
setrecursionlimit(10**4) # don't judge me

from grid import read_stdin
grid, guard = read_stdin("^")
grid[guard] = "."
total = 0

def step(row, col, face):
    if (row, col) not in grid:
        return True # reached edge
    if grid[(row, col)] == "#":
        return False # time to turn
    if grid[(row, col)] == ".":
        grid[(row, col)] = True
        global total
        total += 1
    #if grid[coord] == True:
    if face == "^":
        if not step(row-1, col, face):
            return step(row, col+1, ">")
    if face == ">":
        if not step(row, col+1, face):
            return step(row+1, col, "v")
    if face == "v":
        if not step(row+1, col, face):
            return step(row, col-1, "<")
    if face == "<":
        if not step(row, col-1, face):
            return step(row-1, col, "^")
    return True

step(*guard, "^")
print(total)