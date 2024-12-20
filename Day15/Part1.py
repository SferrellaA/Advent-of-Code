from sys import argv

grid = {}
instructions = []
rrow, rcol = 0, 0
rmax, cmax = 0, 0

stage = 1
row = 0
for line in open(argv[1], 'r').readlines():
    line = line.strip()
    if "#" in line:
        row += 1
        col = 0
        for x in list(line):
            col += 1
            if x == '.':
                x = None
            if x == '@':
                rrow, rcol = row, col
            grid[(row, col)] = x
        cmax = len(line) + 1
    else:
        instructions += list(line)
rmax = row + 1

def show(instruction):
    global grid
    global rmax
    global cmax
    display = ""
    for r in range(1, rmax):
        for c in range(1, cmax):
            if grid[(r, c)] == None:
                display += " "
            else:
                display += grid[(r, c)]
        display += "\n"
    display += instruction + "\n"
    print(display)

def move(row, col, direction):
    global grid

    if grid[(row, col)] == None:
        return True
    if grid[(row, col)] == "#":
        return False
    
    nrow, ncol = row, col
    if direction == '<':
        ncol -= 1
    elif direction == 'v':
        nrow += 1
    elif direction == '>':
        ncol += 1
    elif direction == '^':
        nrow -= 1
    
    if move(nrow, ncol, direction):
        grid[(nrow, ncol)] = grid[(row, col)]
        if grid[(row, col)] == '@':
            global rrow, rcol
            rrow, rcol = nrow, ncol
        grid[(row, col)] = None
        return True

    return False

def gps(row, col):
    global grid
    if grid[(row, col)] != "O":
        return 0
    return (100 * (row-1)) + (col-1)

#show('x')
for i in instructions:
    move(rrow, rcol, i)
    #show(i)
total = 0
for key in grid:
    total += gps(*key)
print(total)