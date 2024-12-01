#!/usr/bin/env python3
#import sys

noun = 25 #int(sys.argv[1])
verb = 5 #int(sys.argv[2])
array = [int(i) for i in open("input.txt").read().split(',')]

def execIndex(index):
	if array[index] == 1:
		array[array[index + 3]] = array[array[index + 1]] + array[array[index + 2]]
	elif array[index] == 2:
		array[array[index + 3]] = array[array[index + 1]] * array[array[index + 2]]
	elif array[index] == 99:
		print(array[0])
		return True
	else:
		print("Cannot Exec", index, ":", array[index])
	return False


array[1] = noun
array[2] = verb
for i in range(len(array[::4])):
	if execIndex(i*4):
		print(100 * noun + verb)
		break