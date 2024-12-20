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



quad = {
    0: 0, # on the middle axis
    1: 0,
    2: 0,
    3: 0,
    4: 0
}
for line in open(argv[1], 'r').readlines():
    p, v = line.split()
    c, r = p.split("=")[1].split(",")
    cd, rd = v.split("=")[1].split(",")
    
    r = robot(r, c, rd, cd)
    r.move(100)
    #print(f"{r.quad()}   {r}")
    quad[r.quad()] += 1

#print(quad[1], quad[2], quad[3], quad[4])
print(quad[1] * quad[2] * quad[3] * quad[4])
# 11 wide, 7 tall
#224054732 is too high