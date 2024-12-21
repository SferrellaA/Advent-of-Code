# sample 1 is 7036
# sample 2 is 11048

# turn 90d for 1000
# step forward for 1
# face east to start

from sys import argv

maze = {}
mrow, mcol = 0, 0
srow, scol = 0, 0
erow, ecol = 0, 0

row = 0
for line in open(argv[1], 'r').readlines():
    row += 1
    for col, val in enumerate(list(line.strip())):
        col += 1
        maze[(row, col)] = val
        if val == 'S':
            srow, scol = row, col
        if val == 'E':
            erow, ecol = row, col
        mcol = col
mrow = row

def step(row, col, path):
    global maze
    if maze[(row, col)] == "#":
        return None
    