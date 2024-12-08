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
failures = []

while True:
    facing = ahead(row, col, face)
    #print((row, col, face))
    if facing not in grid:
        break
    if grid[facing] == "#":
        face = rotate(face)
        continue
    if facing not in blockers and facing not in failures:
        if scan(row, col, face):
            blockers.append(facing)
        else:
            failures.append(facing)
    row, col = facing

print(len(blockers))       
# man this one was bullshit