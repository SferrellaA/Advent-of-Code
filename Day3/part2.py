#!/usr/bin/python
from sys import exit

vals = {(0, 0): 1}
path = 1
puzzle_input = 325489

def setVal(x, y):
    global path, vals

    sum = 0
    try:
        sum += vals[(x-1, y)]
    except:
        pass
    try:
        sum += vals[(x-1, y-1)]
    except:
        pass
    try:
        sum += vals[(x, y-1)]
    except:
        pass
    try:
        sum += vals[(x+1, y-1)]
    except:
        pass
    try:
        sum += vals[(x+1, y)]
    except:
        pass
    try:
        sum += vals[(x+1, y+1)]
    except:
        pass
    try:
        sum += vals[(x, y+1)]
    except:
        pass
    try:
        sum += vals[(x-1, y+1)]
    except:
        pass
    vals[(x, y)] = sum

    path += 1
    if sum > puzzle_input:
        print("%d (%d, %d) -- %d" % (path, x, y, vals[(x, y)]))
        exit(0)

def right(x, y, maxX):
    if x == maxX:
        return x, y
    setVal(x, y)
    return right(x+1, y, maxX)

def up(x, y, maxY):
    if y == maxY:
        return x, y
    setVal(x, y)
    return up(x, y+1, maxY)

def left(x, y, minX):
    if x == minX:
        return x, y
    setVal(x, y)
    return left(x-1, y, minX)

def down(x, y, minY):
    if y == minY:
        return x, y
    setVal(x, y)
    return down(x, y-1, minY)



x = 1
y = 0
r = 1

while True:
    x, y = right(x, y, r)
    x, y = up(x, y, r)
    x, y = left(x, y, -r)
    x, y = down(x, y, -r)
    r += 1

'''
for i in vals:
    print(str(i) + " -- " + str(vals[i]))
'''