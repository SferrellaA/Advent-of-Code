#!/usr/bin/env python3
import time

# Parse parameters from intcode
def parse_parameters(intcode):
    ic = str(intcode)
    op = int(ic[-2:])
    params = [int(i) for i in reversed(ic[:-2])] + [0, 0, 0]  # This isn't elegant
    return op, params


# The class that does everything
class IntCode:
    def __init__(self, code):
        self.code = code
        self.inputs = []
        self.outputs = []
        self.index = 0

    # give an input
    def push_input(self, val: int):
        self.inputs.append(val)

    # get a value
    def get(self, parameter: int, index: int):
        if parameter == 0:  # position mode
            return self.code[self.code[index]]
        if parameter == 1:  # immediate mode
            return self.code[index]

    # set a value
    def set(self, parameter: int, index: int, value: int):
        if parameter == 0:  # position mode
            self.code[self.code[index]] = value
        if parameter == 1:  # immediate mode
            print("Set should always be positional!", parameter, index, value)

    # exec a particular index, return positions to move
    def exec_index(self, index: int):

        # Get the opcode and parameters
        op, params = parse_parameters(self.code[index])

        # Easier to read
        iX = index + 1
        pX = params[0]
        iY = index + 2
        pY = params[1]
        iZ = index + 3
        pZ = params[2]

        # Add X and Y to Z
        if op == 1:
            self.set(pZ, iZ, self.get(pX, iX) + self.get(pY, iY))
            return 4 + index

        # Mul X and Y to Z
        if op == 2:
            self.set(pZ, iZ, self.get(pX, iX) * self.get(pY, iY))
            return 4 + index

        # Store input to X
        if op == 3:
            if len(self.inputs) < 1:
                return -3
            self.set(pX, iX, self.inputs.pop(0))
            return 2 + index

        # Output value at X
        if op == 4:
            self.outputs.append(self.get(pX, iX))
            return 2 + index

        # If X is true (non-zero), jump to Y
        if op == 5:
            if 0 != self.get(pX, iX):
                return self.get(pY, iY)
            return 3 + index

        # If X is false (0), jump to Y
        if op == 6:
            if 0 == self.get(pX, iX):
                return self.get(pY, iY)
            return 3 + index

        # If X is less than Y, write 1 to Z, else 0
        if op == 7:
            if self.get(pX, iX) < self.get(pY, iY):
                self.set(pZ, iZ, 1)
            else:
                self.set(pZ, iZ, 0)
            return 4 + index

        # If X equals Y, write 1 to Z, else 0
        if op == 8:
            if self.get(pX, iX) == self.get(pY, iY):
                self.set(pZ, iZ, 1)
            else:
                self.set(pZ, iZ, 0)
            return 4 + index

        # End Of File
        if op == 99:
            return -99

        # Catch-all for unknown intcode
        print("Unknown intcode:", self.code[index])
        return -1

    # execute all intcode
    def exec(self):
        self.outputs = []
        while self.index < len(self.code):
            x = self.exec_index(self.index)
            if x > 0:      # a valid index to move to
                self.index = x
            elif x == -3:  # needs inputs
                return 3, self.outputs
            elif x == -99: # reached end of execution
                return 99, self.outputs
            else:          # invalid index
                break


# The amplifier class
class Amplifier:
    def __init__(self, intcode):
        self.intcode = IntCode(intcode)
        self.phase = 0

    def run(self):
        return self.intcode.exec()

    def input(self, val):
        self.intcode.push_input(val)



# Return every permutation of a list
def permutation(list):
    if len(list) == 0:
        return []
    if len(list) == 1:
        return [list]
    p = []
    for i in range(len(list)):
        x = list[i]
        y = list[:i] + list[i+1:]
        for z in permutation(y):
            p.append([x] + z)
    return p


# Let's find our answer
# amp = Amplifier([int(i) for i in open("input.txt").read().split(',')])
code = [int(i) for i in open("input.txt").read().split(',')]
highest = 0
for perm in permutation([5, 6, 7, 8, 9]):
    amps = []
    for phase in perm:
        amp = Amplifier(code)
        amp.input(phase)
        amps.append(amp)
    amps[0].input(0)

    vals = []
    while True:
        x = -3
        for amp in amps:
            for v in vals:
                amp.input(v)
            x, vals = amp.run()
        if x == 99:
            break
    if vals[0] > highest:
        highest = vals[0]
print(highest)
