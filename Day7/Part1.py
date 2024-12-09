'''
190: 10 19 has only one position that accepts an operator: between 10 and 19. Choosing + would give 29, but choosing * would give the test value (10 * 19 = 190).
3267: 81 40 27 has two positions for operators. Of the four possible configurations of the operators, two cause the right side to match the test value: 81 + 40 * 27 and 81 * 40 + 27 both equal 3267 (when evaluated left-to-right)!
292: 11 6 16 20 can be solved in exactly one way: 11 + 6 * 16 + 20
'''

from sys import stdin
calibrations = []
for line in stdin:
    line = line.split()
    calibrations.append((int(line[0][:-1]), [int(l) for l in line[1:]]))

calibration = 0

def evaluate(value, target, operators, operands):
    global calibration
    # There goes my attempt to spare some cycles...
    # Too tired to tell whaat this is doing that casues it to skip things that work
    #if value + sum(operators) > target:
    #    return False

    if operators == []:
        if value == target:
            print(f"\t{operands}")
            calibration += target
            return True
        return False
    
    if evaluate(value * operators[0], target, operators[1:], operands + ["*"]):
        return True
    return evaluate(value + operators[0], target, operators[1:], operands + ["+"])

for equation in calibrations:
    target, operators = equation
    print(equation)
    evaluate(operators[0], target, operators[1:], [])

print(calibration)
# 20665820890776 also too low
# 20665820948644 is too low
# 20665830408335