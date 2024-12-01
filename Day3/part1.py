from sys import argv

array = [line.replace('\n','') for line in open(argv[1]).readlines()]

def checkAdjacent(row, column):
    for spot in [(row-1, column),
    (row-1, column+1),
    (row, column+1),
    (row+1, column+1),
    (row+1, column),
    (row+1, column-1),
    (row, column-1),
    (row-1, column-1)]:
        try:
            x = array[spot[0]][spot[1]]
            if not x.isdigit() and x != '.':
                return True
        except:
            pass
    return False

total = 0
for row in range(len(array)):
    tempCount = 0
    tempPart = False
    for column in range(len(array[row])):
        #print(row, column, array[row][column])
        if array[row][column].isdigit():
            tempCount *= 10
            tempCount += int(array[row][column])
            if checkAdjacent(row, column):
                tempPart = True
        else:
            if tempPart:
                total += tempCount
            tempCount = 0
            tempPart = False
    if tempPart:
        total += tempCount
        tempCount = 0
        tempPart = False
print(total)
