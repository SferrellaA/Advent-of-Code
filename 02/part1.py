#!/usr/bin/env python3

array = [int(i) for i in open("input.txt").read().split(',')]

def execIndex(index):
	if array[index] == 1:
		array[array[index + 3]] = array[array[index + 1]] + array[array[index + 2]]
	elif array[index] == 2:
		array[array[index + 3]] = array[array[index + 1]] * array[array[index + 2]]
	elif array[index] == 99:
		print(array[0])
		return
	else:
		print("Cannot Exec", index, ":", array[index])

array[1] = 12
array[2] = 2
for i in range(len(array[::4])):
	execIndex(i*4)