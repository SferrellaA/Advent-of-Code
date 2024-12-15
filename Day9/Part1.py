'''
2333133121414131402
00...111...2...333.44.5555.6666.777.888899
0099811188827773336446555566..............
1928
'''

from sys import argv
disk = [int(i) for i in list(open(argv[1], 'r').read().strip())]
#print(disk)
fileid = 0
for i, val in enumerate(disk):
    if val == 0:
        disk[i] = []
    if i % 2 == 0: # file
        disk[i] = [fileid] * val
        fileid += 1
    else: # space
        disk[i] = [None] * val
disk = sum(disk, [])
#print(disk)
total = 0
for i, val in enumerate(disk):
    while disk[-1] == None:
        disk.pop(-1)
    if val == None:
        #print(i, len(disk))
        try:
            disk[i], disk[-1] = disk[-1], disk[i]
        except:
            # you're done if out of bounds
            break
    total += (i * disk[i])
#print(disk)
print(total)
