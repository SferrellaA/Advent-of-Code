# there are 18 matches in the sample
from sys import stdin

grid = {}
row = -1
starts = []
for line in stdin:
    row += 1
    for column, letter in enumerate([c for c in line.strip("\n")]):
        grid[(row, column)] = letter
        if letter == "X":
            starts.append((row, column))

'''
def target(row, column):
    up = [(row, column), (row-1, column), (row-2, column), (row-3, column)]
    down = [(row, column), (row+1, column), (row+2, column), (row+3, column)]
    left = [(row, column), (row, column-1), (row, column-2), (row, column-3)]
    right = [(row, column), (row, column+1), (row, column+2), (row, column+3)]
    diag_up_right = [(row, column), (row-1, column+1), (row-2, column+2), (row-3, column+3)]
    diag_down_right = [(row, column), (row+1, column+1), (row+2, column+2), (row+3, column+3)]
    diag_down_left = [(row, column), (row+1, column-1), (row+2, column-2), (row+3, column-3)]
    diag_up_left = [(row, column), (row-1, column-1), (row-2, column-2), (row-3, column-3)]
    return [up, down, left, right]
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

def check(X, M, A, S):
    try:
        if grid[X] == "X" and grid[M] == "M" and grid[A] == "A" and grid[S] == "S":
            return True
    except:
        pass
    return False

count = 0
for coord in starts:
    for t in target(*coord):
        if check(*t):
            count += 1
print(count)