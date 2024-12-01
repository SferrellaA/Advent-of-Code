#!/usr/bin/python

minX = 0
curX = 0
maxX = 0

minY = 0
curY = 0
maxY = 0

#values = {(curX, curY): 1}

for i in range(1, 10):
    #print("%d -- %d:%d:%d, %d:%d:%d" % (i, minX, curX, maxX, minY, curY, maxY))
    print("%d -- (%d, %d)" % (i, curX, curY))

    # Bottom
    if curY == minY:
        curX += 1
        if curX > maxX:
            i += 1
            print("   bottom right")
            maxX = curX
            curY += 1
        continue

    # Right
    if curX == maxX:
        curY += 1
        if curY > maxY:
            i += 1
            print("   top right")
            maxY = curY
            curX -= 1
        continue

    # Top
    if curY == maxY:
        curX -= 1
        if curX < minX:
            i += 1
            print("   top left")
            minX = curX
            curY -= 1
        continue

    # Left
    if curX == minX:
        curY -= 1
        if curY < minY:
            i += 1
            print("   bottom left")
            minY = curY
            curX += 1
        continue
        
            
    print("Uh oh")



    