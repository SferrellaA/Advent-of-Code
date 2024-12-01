#!/usr/bin/env python3

# Check if a given number has proper doubles
def check_doubles(number):
    number = [-1] + number + [-1]
    for i, j in enumerate(number):
        try:
            if number[i] == number[i+1]:
                if number[i-1] != number[i]:
                    if number[i+2] != number[i]:
                        return True
        except IndexError:
            pass

# Check if a given number just increases
def check_increasing(number):
    for i, j in enumerate(number):
        try:
            if number[i] > number[i+1]:
                return False
        except IndexError:
            pass
    return True
# 1071 is too low, but 1232 is too high

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
    if check_increasing(array[0]):
        if check_doubles(array[0]):
            print(array[0])
            total += 1
    if array[0] == array[1]:
        print(total)
        break