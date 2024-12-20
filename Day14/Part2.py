from sys import argv
if len(argv) < 4:
    print("Not enough arguments!")
    print("python script.py sample.txt $width $height")
    exit()

wide = int(argv[2])
tall = int(argv[3])
print(f"Grid is {wide} wide, {tall} tall")

class robot:
    def __init__(self, row, col, row_delta, col_delta):
        self.row = int(row)
        self.col = int(col)
        self.rdel = int(row_delta)
        self.cdel = int(col_delta)

    def __str__(self):
        return f"p({self.row},{self.col}) v({self.rdel},{self.cdel})"

    def move(self, seconds):
        # got it ncie now!
        global wide
        global tall
        self.row = (self.row + (self.rdel * seconds)) % tall
        self.col = (self.col + (self.cdel * seconds)) % wide

        '''
        self.row += (self.rdel * seconds)
        if self.row < 0 or self.row > tall:
            #self.row += (tall * abs(int(self.row / tall)))
            self.row = self.row % tall
        #if self.row > tall:
        #    self.row = self.row % tall
        
        self.col += (self.cdel * seconds)
        if self.col < 0 or self.col > wide:
            self.col = self.col % wide
        '''
        '''
        # Not efficient but I dont have any paper to do algebra with
        for _ in range(seconds):
            self.rcur += self.rdel
            if self.rcur < 0:
                self.rcur += tall
            elif self.rcur > tall:
                self.rcur -= tall
            self.ccur += self.cdel
            if self.ccur < 0:
                self.ccur += wide
            elif self.ccur > wide:
                self.ccur -= wide
        '''

    def quad(self):
        global wide
        global tall
        # 7 tall x 11 wide -> 3 htall x 5 hwide
        hwide = int(wide/2)
        htall = int(tall/2)
        if self.row < htall and self.col < hwide:
            return 1
        if self.row < htall and self.col > hwide:
            return 2
        if self.row > htall and self.col < hwide:
            return 3
        if self.row > htall and self.col > hwide:
            return 4
        
        return 0

robots = []
for line in open(argv[1], 'r').readlines():
    p, v = line.split()
    c, r = p.split("=")[1].split(",")
    cd, rd = v.split("=")[1].split(",")
    robots.append(robot(r, c, rd, cd))
    #r.move(100)
    #print(f"{r.quad()}   {r}")
    #quad[r.quad()] += 1

def display(robots):
    global wide
    global tall
    tree = {}
    art = ""
    for r in robots:
        tree[(r.row, r.col)] = True
    for row in range(tall):
        for col in range(wide):
            if (row, col) in tree:
                art += "+"
            else:
                art += ' '
        art += "\n"
    return art

seconds = 0
while True:
    tree = display(robots)
    if "++++++++++" in tree: # cheated to find what I was supposed to be looking for
        print(tree)
        print(f"\n=== {seconds} ===")
        input()
    for r in robots:
        r.move(1)
    seconds += 1