#!/usr/bin/env python3

# Handle a single step direction
def handleC(c):
	global x
	global y
	if c == 'U':
		y += 1
		return
	elif c == 'R':
		x += 1
		return
	elif c == 'D':
		y -= 1
		return
	elif c == 'L':
		x -= 1
		return
	print("I got a weird letter:", c)

# The grid system
x = 0
y = 0
grid = {}
grid[(x,y)] = 1

# Set the first grid
coord = [line.split(',') for line in open('input.txt').read().split()]
for c in coord[0]:
	for i in range(int(c[1:])):
		handleC(c[0])
		grid[(x,y)] = 1

# Then see where the second grid overlaps
x = 0
y = 0
overlaps = {}
for c in coord[1]:
	for i in range(int(c[1:])):
		handleC(c[0])
		if (x, y) in grid.keys():
			overlaps[abs(x) + abs(y)] = (x, y)

# Print the coordinates with the shortest distance
z = min(overlaps)
print(z, overlaps[z])