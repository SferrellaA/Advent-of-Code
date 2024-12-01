#!/usr/bin/env python3
import math

def calc(mass):
    fuel = math.floor(mass / 3) - 2
    if fuel > 0:
        return fuel + calc(fuel)
    return 0
    
total = 0
for line in open('input.txt').read().split():
    total += calc(int(line))
print(total)