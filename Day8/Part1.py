from sys import stdin

width = 0
height = 0
city = {}

for line in stdin:
    line = list(line.strip())
    width = len(line)
    height += 1

    for col, val in enumerate(line):
        if val == '.':
            continue
        if val not in city:
            city[val] = []
        city[val].append((height, col+1))

def gonkulate(one, two):
    one_r, one_c = one
    two_r, two_c = two
    del_r = abs(one_r - two_r)
    del_c = abs(one_c - two_c)
    if one_r > two_r:
        one_r += del_r
        two_r -= del_r
    else:
        one_r -= del_r
        two_r += del_r
    if one_c > two_c:
        one_c += del_c
        two_c -= del_c
    else:
        one_c -= del_c
        two_c += del_c
    return (one_r, one_c), (two_r, two_c)

'''
print(column, row)
for key in grid:
    print(key, grid[key])
'''

antinodes = []
for frequency in city:
    for pos1 in city[frequency]:
        for pos2 in city[frequency]:
            if pos1 == pos2:
                continue
            antinodes += [*gonkulate(pos1, pos2)]
antinodes = list(set(antinodes))
counted = 0
for antinode in antinodes:
    r, c = antinode
    if 1 <= r and r <= height:
        if 1 <= c and c <= width:
            counted += 1
print(counted)