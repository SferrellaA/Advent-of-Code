from sys import stdin
calibrations = []
for line in stdin:
    line = line.split()
    calibrations.append((int(line[0][:-1]), [int(l) for l in line[1:]]))

calibration = 0

def evaluate(value, target, operators, operands):
    if operators == []:
        if value == target:
            global calibration
            calibration += target
            return True
        return False
    
    if evaluate(value * operators[0], target, operators[1:], operands + ["*"]):
        return True
    if evaluate(value + operators[0], target, operators[1:], operands + ["+"]):
        return True
    if evaluate(int(f"{value}{operators[0]}"), target, operators[1:], operands + ["||"]):
        return True
    return False

for equation in calibrations:
    target, operators = equation
    evaluate(operators[0], target, operators[1:], [])

print(calibration)