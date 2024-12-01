#!/usr/bin/env python
total = 0
for line in open('input.txt').read().split():
    total += ((int(line) / 3) - 2)
print(total)