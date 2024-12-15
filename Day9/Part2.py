'''
2333133121414131402
00...111...2...333.44.5555.6666.777.888899
0099.111...2...333.44.5555.6666.777.8888..
0099.1117772...333.44.5555.6666.....8888..
0099.111777244.333....5555.6666.....8888..
00992111777.44.333....5555.6666.....8888..
2858
'''

from sys import argv
disk = [int(i) for i in list(open(argv[1], 'r').read().strip())]
fileid = 0
for i, val in enumerate(disk):
    if i % 2 == 0: # file
        disk[i] = [fileid] * val
        fileid += 1
    else: # space
        disk[i] = (None, val)
print(disk)
print()
for i, v in enumerate(disk):
    if type(v) is list:
        continue
    for j, r in enumerate(reversed(disk)):
        ival, ilen = v
        jval, jlen = r
        if jlen <= ilen:
            ilen -= jlen
            disk.insert(i, r)
            disk.remove(r)
            break
    #disk[i] = [0] * v[1]
print(disk)

exit()
#disk = sum(disk, [])

