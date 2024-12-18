from sys import stdin

class game:
    def __init__(self):
        self.aC = 0
        self.bC = 0
        pass
    def addA(self, x, y):
        self.ax = x
        self.ay = y
    def addB(self, x, y):
        self.bx = x
        self.by = y
    def addPrize(self, x, y):
        self.px = x
        self.py = y
    def A(self, x, y):
        if self.bC == 100:
            return None
        self.aC += 1
        return (x + self.ax, y + self.ay)
    def B(self, x, y):
        if self.bC == 100:
            return None
        self.bC += 1
        return (x + self.bx, y + self.by)
    def __str__(self):
        s =  f"A: {self.ax}, {self.ay}\n"
        s += f"B: {self.bx}, {self.by}\n"
        s += f"P: {self.px}, {self.py}\n"
        s += f"   A x{self.aC}, B x{self.bC}\n"
        return s

def parse(line):
    line = line.split(":")[1]
    line = line.split(", ")
    try:
        line = [l.split("+")[1] for l in line]
    except:
        line = [l.split("=")[1] for l in line]
    line = [int(l) for l in line]
    return line

g = game()
for line in stdin:
    line = line.strip()
    if line == "":
        print(g)
        g = None
        g = game()
        continue
    x, y = parse(line)
    if "A:" in line:
        g.addA(x, y)
    elif "B:" in line:
        g.addB(x, y)
    elif "Prize:" in line:
        g.addPrize(x, y)

'''
The cheapest way to win the prize is by pushing the A button 80 times and the B button 40 times. This would line up the claw along the X axis (because 80*94 + 40*22 = 8400) and along the Y axis (because 80*34 + 40*67 = 5400). Doing this would cost 80*3 tokens for the A presses and 40*1 for the B presses, a total of 280 tokens.

For the second and fourth claw machines, there is no combination of A and B presses that will ever win a prize.

For the third claw machine, the cheapest way to win the prize is by pushing the A button 38 times and the B button 86 times. Doing this would cost a total of 200 tokens.

So, the most prizes you could possibly win is two; the minimum tokens you would have to spend to win all (two) prizes is 480.
'''

