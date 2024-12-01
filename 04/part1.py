#!/usr/bin/env python3


# Check if a given number has doubles
def check_valid(number):
    doubles = False
    for i, j in enumerate(number):
        try:
            if number[i+1] < number[i]:
                return False
            if number[i+1] == number[i]:
                doubles = True
        except:
            pass
    return doubles


# Add one
def add_one(number):
    for i, j in reversed(list(enumerate(number))):
        if j < 9:
            number[i] += 1
            for i in range(i + 1, len(number)):
                number[i] = 0
            break
    return number


# Set up the puzzle input
puzzle = "206938-679128"
array = []
for side in puzzle.split('-'):
    x = []
    for i in side:
        x.append(int(i))
    array.append(x)

# Just brute force it
total = 0
while True:
    array[0] = add_one(array[0])
    if check_valid(array[0]):
        total += 1
    if array[0] == array[1]:
        print(total)
        break