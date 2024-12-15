from sys import stdin

width = 0
height = 0
city = {}
antinodes = []

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
        antinodes.append((height, col+1))

def gonkulate(one, two):
    base_r, base_c = one
    delta_r, delta_c = two
    delta_r -= base_r
    delta_c -= base_c
    coords = []
    global width
    global height
    for step in range(width):
        r1 = base_r + (delta_r * step)
        r2 = base_r - (delta_r * step)
        c1 = base_c + (delta_c * step)
        c2 = base_c - (delta_c * step)
        if 1 <= r1 and r1 <= height:
            if 1 <= c1 and c1 <= width:
                coords.append((r1, c1))
        if 1 <= r2 and r2 <= height:
            if 1 <= c2 and c2 <= width:
                coords.append((r2, c2))
    return coords

for frequency in city:
    for pos1 in city[frequency]:
        for pos2 in city[frequency]:
            if pos1 == pos2:
                continue
            antinodes += gonkulate(pos1, pos2)
antinodes = list(set(antinodes))
#print(antinodes)
print(len(antinodes))