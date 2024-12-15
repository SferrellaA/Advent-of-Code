from sys import argv
disk = [int(i) for i in list(open(argv[1], 'r').read().strip())]
rev = []
fileid = 0
for i, val in enumerate(disk):
    if i % 2 == 0: # file
        disk[i] = (fileid, val)
        rev.insert(0, (fileid, val))
        fileid += 1
    else: # space
        disk[i] = (None, val)

def print_disk():
    global disk
    flat = []
    for thing in disk:
        fid, size = thing
        if size == 0:
            continue
        if fid == None:
            fid = '.'
        else:
            fid = f'{fid}'
        flat += [fid] * size
    print()
    print(''.join(flat))

'''
2333133121414131402
00...111...2...333.44.5555.6666.777.888899
0099.111...2...333.44.5555.6666.777.8888..
0099.1117772...333.44.5555.6666.....8888..
0099.111777244.333....5555.6666.....8888..
00992111777.44.333....5555.6666.....8888..
2858
'''

#print_disk()
for r in rev:
    rfid, rsize = r
    j = disk.index(r)+1
    for i in range(j):
        ifid, isize = disk[i]
        if ifid is not None:
            continue
        if rsize <= isize:
            disk[i] = (None, isize-rsize)
            disk.insert(i, (None, rsize))
            disk[i], disk[j] = disk[j], disk[i]
            break
    #print_disk()

total = 0
index = 0
for thing in disk:
    fid, size = thing
    if fid == None:
        fid = 0
    for i in range(size):
        total += (index * fid)
        index += 1
print(total)