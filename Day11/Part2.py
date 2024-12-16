from sys import argv
stones = [int(s) for s in open(argv[1], 'r').read().split()]

#hashes = {}

def blink(stones):
    inserts = []
    for i, stone in enumerate(stones):
        if stone == 0:
            stones[i] = 1
            continue
        #if stone in hashes:
        #    stones[i] = hashes[stone]
        #    continue
        s = list(str(stone))
        if len(s) % 2 == 0:
            new = s[:int(len(s)/2)]
            stone = s[int(len(s)/2):]
            new = int(''.join(new))
            stone = int(''.join(stone))
            stones[i] = stone
            inserts.append(new)
            #hashes[stone] = [new, stone]
            continue
        stones[i] *= 2024
    stones += inserts

for i in range(75):
    print(f"Blink {i}")
    blink(stones)
print()
print(len(stones))